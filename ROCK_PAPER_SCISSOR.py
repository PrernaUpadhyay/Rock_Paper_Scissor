import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List to store the choices as strings
choices = [rock, paper, scissors]

# Get user input and convert it to an integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Ensure valid input
if user_choice < 0 or user_choice > 2:
    print("Invalid choice! Please choose 0, 1, or 2.")
else:
    # Generate computer choice
    computer_choice = random.randint(0, 2)

    # Print user and computer choices
    print(f"\nYou chose:\n{choices[user_choice]}")
    print(f"Computer chose:\n{choices[computer_choice]}")

    # Determine the result
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
