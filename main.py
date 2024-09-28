import random
import tkinter as tk
from tkinter import messagebox

# Main Game Logic
def determine_winner(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = f"You win! {user_choice} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice} beats {user_choice}."
    
    messagebox.showinfo("Result", result)

# GUI Functionality
def play_rock():
    determine_winner('Rock')

def play_paper():
    determine_winner('Paper')

def play_scissors():
    determine_winner('Scissors')

# Set up the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create buttons
rock_button = tk.Button(window, text="Rock", width=15, height=2, command=play_rock)
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=15, height=2, command=play_paper)
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, command=play_scissors)
scissors_button.pack(pady=10)

# Run the application
window.mainloop()
