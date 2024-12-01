from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from slugify import slugify as slugify_function

def create_motivational_images(quotes, authors, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set a fixed image size
    img_width = 800
    img_height = 800

    for quote, author in zip(quotes, authors):
        # Create a blank image with a background color
        img = Image.new('RGB', (img_width, img_height), color=(73, 109, 137))

        # Load a font and initialize font size
        font_size = 40  # Set a larger default font size
        font = ImageFont.truetype("arial.ttf", font_size)
        draw = ImageDraw.Draw(img)
        
        # Set max width for text wrapping
        max_text_width = img_width * 0.8

        # Wrap the text to fit within the max width
        wrapped_text = textwrap.fill(quote, width=40)

        # Get text dimensions after wrapping using textbbox()
        quote_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        quote_width, quote_height = quote_bbox[2] - quote_bbox[0], quote_bbox[3] - quote_bbox[1]
        
        author_bbox = draw.textbbox((0, 0), f"- {author}", font=font)
        author_width, author_height = author_bbox[2] - author_bbox[0], author_bbox[3] - author_bbox[1]

        # Calculate position to center the text
        total_text_height = quote_height + author_height + 20  # Add space between quote and author
        y_quote = (img_height - total_text_height) // 2
        y_author = y_quote + quote_height + 10

        # Draw the wrapped quote and author
        draw.text(((img_width - quote_width) // 2, y_quote), wrapped_text, font=font, fill=(255, 255, 255))
        draw.text(((img_width - author_width) // 2, y_author), f"- {author}", font=font, fill=(255, 255, 255))

        # Save the image
        filename = f"{slugify_function(quote)}_{slugify_function(author)}.png"
        img.save(os.path.join(output_dir, filename))

# Example usage:
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "The best way to predict the future is to create it.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "It does not matter how slowly you go, as long as you do not stop.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "You are never too old to set another goal or to dream a new dream.",
    "The secret of getting ahead is getting started.",
    "You miss 100% of the shots you don’t take.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Do what you can, with what you have, where you are.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "You only live once, but if you do it right, once is enough.",
    "If you want to lift yourself up, lift up someone else.",
    "The only place where success comes before work is in the dictionary.",
    "Dream big and dare to fail.",
    "It does not matter how slowly you go, as long as you do not stop.",
    "Act as if what you do makes a difference. It does.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "To be successful, you must accept all challenges that come your way.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Push yourself to do more and to experience more.",
    "Wake up with a purpose.",
    "Be so good they can’t ignore you.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Don’t wait for opportunity. Create it.",
    "The harder you work, the luckier you get.",
    "Success is a journey, not a destination.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Opportunities don't happen. You create them.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Hard work beats talent when talent doesn’t work hard.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Your only limit is your mind.",
    "Success doesn’t come from what you do occasionally. It comes from what you do consistently."
]

authors = [
    "Theodore Roosevelt",
    "Steve Jobs",
    "Winston Churchill",
    "Sam Levenson",
    "Abraham Lincoln",
    "Winston Churchill",
    "Confucius",
    "Franklin D. Roosevelt",
    "C.S. Lewis",
    "Mark Twain",
    "Wayne Gretzky",
    "C.S. Lewis",
    "Eleanor Roosevelt",
    "Theodore Roosevelt",
    "Steve Jobs",
    "Nelson Mandela",
    "Albert Schweitzer",
    "Anonymous",
    "Unknown",
    "Walt Disney",
    "Albert Einstein",
    "Robert F. Kennedy",
    "Mahatma Gandhi",
    "Thomas Edison",
    "Anonymous",
    "Steve Young",
    "Mahatma Gandhi",
    "Anonymous",
    "Albert Schweitzer",
    "Anonymous",
    "Anonymous",
    "Anonymous",
    "Unknown",
    "Anonymous",
    "Thomas Edison",
    "Anonymous",
    "Anonymous",
    "Albert Einstein",
    "Anonymous",
    "Henry Ford",
    "Les Brown",
    "Robert H. Schuller",
    "Oprah Winfrey",
    "Unknown",
    "Ralph Waldo Emerson",
    "Tony Robbins",
    "Anonymous",
    "Anonymous",
    "Anonymous",
    "Anonymous"
]


output_dir = "motivational_images"
create_motivational_images(quotes, authors, output_dir)

print("Script end")
