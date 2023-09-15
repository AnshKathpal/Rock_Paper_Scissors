import random

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Stone Paper Scissors!")
    print("---------------------------------")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("---------------------------------------------------------------------")
    print("Enter your choice: rock, paper, or scissors")
    print("---------------------------------------------")
    print("To quit the game, type 'quit'")
    print("------------------------------")

    while True:
        user_choice = input("Your choice: ").lower()
        computer_choice = random.choice(choices)

        if user_choice == "quit":
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print("Score: You", user_score, "- Computer", computer_score)
        print()

play_game()