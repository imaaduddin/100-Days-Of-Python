import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# choices = [rock, paper, scissors]

# computer_choice = random.choice(choices)

# human_choice = random.choice(choices)

# if human_choice == paper and computer_choice == rock:
#     print(human_choice)
#     print("Humans win!")
# elif computer_choice == paper and human_choice == rock:
#     print(computer_choice)
#     print("Computer wins!")
# if human_choice == rock and computer_choice == scissors:
#     print(human_choice)
#     print("Go humans!")
# elif computer_choice == rock and human_choice == scissors:
#     print(computer_choice)
#     print("Computer wins...")
# if human_choice == scissors and computer_choice == paper:
#     print(human_choice)
#     print("Let's gooo humans!!!")
# elif computer_choice == scissors and human_choice == paper:
#     print(computer_choice)
#     print("Them robots win...")


# Professor solution:
game_images = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_input])

computer_input = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_input])

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, you lose!")
elif user_input == 0 and computer_input == 2:
    print("User Wins!")
elif computer_input == 0 and user_input == 2:
    print("User loses!")
elif computer_input > user_input:
    print("You lose!")
elif user_input > computer_input:
    print("You win!")
elif computer_input == user_input:
    print("It's a draw!")






