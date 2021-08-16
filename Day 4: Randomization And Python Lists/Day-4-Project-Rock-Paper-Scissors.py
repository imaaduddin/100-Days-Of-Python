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

choices = [rock, paper, scissors]

computer_choice = random.choice(choices)

human_choice = random.choice(choices)

if human_choice == paper and computer_choice == rock:
    print(human_choice)
    print("Humans win!")
elif computer_choice == paper and human_choice == rock:
    print(computer_choice)
    print("Computer wins!")
if human_choice == rock and computer_choice == scissors:
    print(human_choice)
    print("Go humans!")
elif computer_choice == rock and human_choice == scissors:
    print(computer_choice)
    print("Computer wins...")
if human_choice == scissors and computer_choice == paper:
    print(human_choice)
    print("Let's gooo humans!!!")
elif computer_choice == scissors and human_choice == paper:
    print(computer_choice)
    print("Them robots win...")









