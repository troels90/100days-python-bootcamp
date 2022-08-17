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

#Write your code below this line 👇
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
comp_choice = random.randint(0,2)
player_choice_int = int(player_choice)
rps_str = ["Rock", "Paper", "Scissors"]
rps_gfx = [rock, paper, scissors]


print("You chose " + rps_str[player_choice_int] + rps_gfx[player_choice_int])

print("Computer chose " + rps_str[comp_choice] + rps_gfx[comp_choice])

diff_choice = player_choice_int - comp_choice

if diff_choice == 0:
  print("It's a draw!")
elif diff_choice == 1 or diff_choice == -2:
  print(" ! You won! ")
elif diff_choice == -1 or diff_choice == 2:
  print("You lost!")