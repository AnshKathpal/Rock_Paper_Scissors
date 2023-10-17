import tkinter as tk
import random

# Define global variables
user_wins = None
computer_wins = None
draws = None
user_choice_var = None
result_label = None  # Declare result_label as a global variable

def play_game():
    global user_wins, computer_wins, draws, user_choice_var, result_label  # Use the global variables

    user_choice = user_choice_var.get()
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    result_label.config(text=f"Computer Chooses: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a draw!")
        draws.set(draws.get() + 1)
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result_label.config(text=f"Congrats! You Win! {user_choice.capitalize()} beats {computer_choice}.")
        user_wins.set(user_wins.get() + 1)
    else:
        result_label.config(text=f"Computer wins! {computer_choice.capitalize()} beats {user_choice}.")
        computer_wins.set(computer_wins.get() + 1)

    score_label.config(text=f"Score: User {user_wins.get()} - Computer {computer_wins.get()} - Draws {draws.get()}")

    user_choice_var.set("")  # Reset user choice

def quit_game():
    root.destroy()

def start_new_game():
    global user_wins, computer_wins, draws, user_choice_var, result_label

    user_wins.set(0)
    computer_wins.set(0)
    draws.set(0)

    # Reset user choice
    user_choice_var.set("")

    # Reset result label
    result_label.config(text="")

def create_game_ui():
    global root, user_wins, computer_wins, draws, user_choice_var, result_label

    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    # Initialize Tkinter variables
    user_wins = tk.IntVar()
    computer_wins = tk.IntVar()
    draws = tk.IntVar()
    user_choice_var = tk.StringVar()

    user_choice_var.set("")  # Reset user choice

    result_label = tk.Label(root, text="", font=("Helvetica", 16))
    result_label.pack(pady=10)

    rock_button = tk.Button(root, text="Rock", command=lambda: user_choice_var.set("rock"))
    paper_button = tk.Button(root, text="Paper", command=lambda: user_choice_var.set("paper"))
    scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice_var.set("scissors"))
    quit_button = tk.Button(root, text="Quit", command=quit_game)

    rock_button.pack()
    paper_button.pack()
    scissors_button.pack()
    quit_button.pack()

    play_button = tk.Button(root, text="Play", command=play_game)
    play_button.pack()

    score_label = tk.Label(root, text=f"Score: User {user_wins.get()} - Computer {computer_wins.get()} - Draws {draws.get()}")
    score_label.pack()

    new_game_button = tk.Button(root, text="Start New Game", command=start_new_game)
    new_game_button.pack()

    root.mainloop()

create_game_ui()
