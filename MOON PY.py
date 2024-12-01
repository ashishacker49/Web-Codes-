from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from datetime import datetime, timedelta
import pandas as pd
from PIL import Image
import os

# Load ephemeris data
ephemeris = load('de421.bsp')

# Define Earth, Moon, and Sun
earth = ephemeris['earth']
moon = ephemeris['moon']
sun = ephemeris['sun']  # Add the Sun to the calculation

# Define date range from today to December 31, 2025
start_date = datetime(2024, 11, 26)
end_date = datetime(2025, 12, 31)
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Zodiac signs (approximate ecliptic longitudes) with Hindi names
zodiac_signs = [
    (0, "Aries", "मेष"), (30, "Taurus", "वृषभ"), (60, "Gemini", "मिथुन"), (90, "Cancer", "कर्क"),
    (120, "Leo", "सिंह"), (150, "Virgo", "कन्या"), (180, "Libra", "तुला"), (210, "Scorpio", "वृश्चिक"),
    (240, "Sagittarius", "धनु"), (270, "Capricorn", "मकर"), (300, "Aquarius", "कुम्भ"), (330, "Pisces", "मीन"), (360, "Aries", "मेष")
]

# Moon phases with English and Hindi names
moon_phases = {
    "New Moon": "नया चाँद",
    "Waxing Crescent": "वर्धमान अर्धचन्द्र",
    "First Quarter": "प्रथम तिमाही",
    "Waxing Gibbous": "वर्धमान गिब्बस",
    "Full Moon": "पूर्ण चाँद",
    "Waning Gibbous": "ह्रासमान गिब्बस",
    "Last Quarter": "अंतिम तिमाही",
    "Waning Crescent": "ह्रासमान अर्धचन्द्र"
}

# Function to determine the zodiac sign based on ecliptic longitude
def get_zodiac_sign(longitude):
    for limit, sign_en, sign_hi in zodiac_signs:
        if longitude < limit:
            return sign_en, sign_hi

# Prepare data
moon_data = []
ts = load.timescale()

# Path to the moon phase images folder
images_dir = r"C:\Users\hp\Desktop\images"



# Function to assign the correct moon phase image
def get_moon_image(phase):
    moon_phase_images = {
        "New Moon": f"{images_dir}/new_moon.png",
        "Waxing Crescent": f"{images_dir}/waxing_crescent.png",
        "First Quarter": f"{images_dir}/first_quarter.png",
        "Waxing Gibbous": f"{images_dir}/waxing_gibbous.png",
        "Full Moon": f"{images_dir}/full_moon.png",
        "Waning Gibbous": f"{images_dir}/waning_gibbous.png",
        "Last Quarter": f"{images_dir}/last_quarter.png",
        "Waning Crescent": f"{images_dir}/waning_crescent.png",
    }
    return moon_phase_images.get(phase, None)

# Function to generate unique tips based on moon phase and zodiac sign
def get_unique_tips(phase, zodiac_en, zodiac_hi):
    tips = []

    if phase == "New Moon":
        tips.append("It's a time for new beginnings. Set intentions for the month ahead.")
        tips.append("A good day for introspection and planning your next steps.")
    elif phase == "Full Moon":
        tips.append("The Full Moon is a time of culmination. Focus on completing tasks.")
        tips.append("Release any negative energy that’s holding you back.")
    elif phase == "First Quarter":
        tips.append("Take action on the plans you set during the New Moon.")
        tips.append("Focus on progress, but be mindful of obstacles.")
    elif phase == "Last Quarter":
        tips.append("Reflect on the lessons of the month and let go of what no longer serves you.")
        tips.append("This is a good time for deep cleansing and healing.")

    if zodiac_en in ["Cancer", "Pisces", "Scorpio"]:  # Water signs
        tips.append("Emotions are heightened today, trust your intuition.")
        tips.append("Focus on your emotional well-being and connect with loved ones.")
    elif zodiac_en in ["Aries", "Leo", "Sagittarius"]:  # Fire signs
        tips.append("Take bold actions and seize the opportunities that come your way.")
        tips.append("Your creativity is at its peak today.")
    elif zodiac_en in ["Taurus", "Virgo", "Capricorn"]:  # Earth signs
        tips.append("Practical decisions will bring long-term stability.")
        tips.append("Focus on creating a strong foundation for the future.")
    elif zodiac_en in ["Gemini", "Libra", "Aquarius"]:  # Air signs
        tips.append("Great day for communication, networking, and sharing ideas.")
        tips.append("Your intellect is sharp—use it to solve problems.")

    # Add Virgo specific tips
    if zodiac_en == "Virgo":
        tips.append("Focus on self-care and organization. Tidy up your surroundings to feel more in control.")
        tips.append("Use the energy of the moon to set practical goals and improve your health routines.")

    return " ".join(tips)

# Loop through dates and gather data
for date in dates:
    t = ts.utc(date.year, date.month, date.day)
    
    # Correct observation code to observe the moon relative to Earth
    moon_position = earth.at(t).observe(moon).apparent()
    ecliptic_position = moon_position.frame_latlon(ecliptic_frame)
    longitude = ecliptic_position[1].degrees % 360

    # Find Moon Phase
    phase_angle = moon_position.phase_angle(sun)  # Correct phase angle calculation
    if phase_angle.degrees < 7:
        phase = "New Moon"
    elif phase_angle.degrees < 90:
        phase = "Waxing Crescent"
    elif phase_angle.degrees < 97:
        phase = "First Quarter"
    elif phase_angle.degrees < 180:
        phase = "Waxing Gibbous"
    elif phase_angle.degrees < 187:
        phase = "Full Moon"
    elif phase_angle.degrees < 270:
        phase = "Waning Gibbous"
    elif phase_angle.degrees < 277:
        phase = "Last Quarter"
    else:
        phase = "Waning Crescent"

    # Get Moon phase image
    moon_image = get_moon_image(phase)

    # Get Zodiac sign (English and Hindi)
    zodiac_en, zodiac_hi = get_zodiac_sign(longitude)

    # Generate unique tips for the day
    tips = get_unique_tips(phase, zodiac_en, zodiac_hi)

    # Append data
    moon_data.append({
        "Date": date.strftime('%Y-%m-%d'),
        "Moon Phase (English)": phase,
        "Moon Phase (Hindi)": moon_phases.get(phase, ""),
        "Zodiac Sign (English)": zodiac_en,
        "Zodiac Sign (Hindi)": zodiac_hi,
        "Moon Phase Image": moon_image,
        "Important Notes": tips
    })

# Create DataFrame and save to Excel
moon_calendar_df = pd.DataFrame(moon_data)
file_path_moon_calendar = "C:/Users/hp/Desktop/Moon_Tracking_Calendar_2024_2025.xlsx"
moon_calendar_df.to_excel(file_path_moon_calendar, index=False)

print(f"Moon phase tracking calendar saved to {file_path_moon_calendar}")
