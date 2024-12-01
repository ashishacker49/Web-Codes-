import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Number Guess Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Create GUI elements
        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.label.pack()

        self.entry = tk.Entry(master, width=20)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        user_guess = int(self.entry.get())
        self.attempts += 1

        if user_guess == self.secret_number:
            self.result_label.config(text=f"Congratulations! You found the secret number in {self.attempts} attempts.")
        elif user_guess < self.secret_number:
            self.result_label.config(text="Too low! Try again.")
        else:
            self.result_label.config(text="Too high! Try again.")

root = tk.Tk()
my_game = GuessingGame(root)
root.mainloop()
