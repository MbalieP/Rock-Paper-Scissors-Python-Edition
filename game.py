
import random

choices = {0: "Rock", 1: "Paper", 2: "Scissors"}


user_choice = int(input("Enter your choice: type 0 for Rock, 1 for Paper, 2 for Scissors: "))


if user_choice >= 3 or user_choice < 0: # Checking if the user's input is valid
    print("You've entered an invalid number, you lose!")
else:
    
    computer_choice = random.randint(0, 2) # Generating the computer choice
    
    
    print(f"You chose: {choices[user_choice]}")
    print(f"The computer chose: {choices[computer_choice]}")
    
    
    if computer_choice == user_choice:
        print("It's a draw!")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer wins, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win, computer loses!")
    elif computer_choice > user_choice:
        print("Computer wins, you lose!")
    elif user_choice > computer_choice:
        print("You win, computer loses!")
