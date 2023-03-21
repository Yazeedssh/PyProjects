import random

user_choice = int(input("which one do you choos? Type 0 for rock, 1 for paper, 2 for scissors: "))

computer_choice = random.randint(0,2)
print(f"The computer choose {computer_choice}")

if user_choice >=3 or user_choice <0:
    print("You typed invalid number!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose );")
elif user_choice == computer_choice:
    print("Draw")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose );")
