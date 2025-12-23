import random


while True:
    options = ["r", "p", "s"]
    computer_choice = random.choice(options)
    choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

    if choice not in options:
        print(f"Computer choice: {computer_choice}")
        print("Not valid")
    elif choice != computer_choice:
        print(f"Computer choice: {computer_choice}")
        print("You lose!")
    else:
        print(f"Computer choice: {computer_choice}")
        print("You win!")
        break