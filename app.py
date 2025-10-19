import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < 40 : 
            self.result_label.config(text="Too low! Try again.")
        elif guess > 40 :
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(
                text=f"Correct! The number was {self.secret_number}. You guessed it in {self.attempts} tries."
            )
            self.guess_button.config(state=tk.DISABLED)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
