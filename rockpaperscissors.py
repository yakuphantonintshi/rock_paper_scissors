import random


while True:
    options = ("r", "p", "s")
    computer_choice = random.choice(options)
    choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

    if choice not in options:
        print(f"Computer choice: {computer_choice}")
        print("Not valid")
    elif choice == "r" and computer_choice == "p":
        print(f"Computer choice: {computer_choice}")
        print("Computer Won!")
    elif choice == "r" and computer_choice == "s":
        print(f"Computer choice: {computer_choice}")
        print("You Won!")
    elif choice == "s" and computer_choice == "r":
        print(f"Computer choice: {computer_choice}")
        print("Computer Won!")
    elif choice == "s" and computer_choice == "p":
        print(f"Computer choice: {computer_choice}")
        print("You Won!")
    elif choice == "p" and computer_choice == "s":
        print(f"Computer choice: {computer_choice}")
        print("Computer Won!")
    elif choice == "p" and computer_choice == "r":
        print(f"Computer choice: {computer_choice}")
        print("You Won!")
    else:
        print(f"Computer choice: {computer_choice}")
        print("It's a Tie!")
        break