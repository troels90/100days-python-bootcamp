import game_data
import art
import random
from replit import clear



DATA_LENGTH = len(game_data.data)-1
positions_used = []

def get_info_data(position):
  hype = ""
  name = game_data.data[position]["name"]
  description = game_data.data[position]["description"]
  country = game_data.data[position]["country"]
  text = (f"{hype} {name}, {description}, from {country}")
  return text

def get_followers(position):
  followers = int(game_data.data[position]["follower_count"])
  return followers
  
def get_position():
  position = random.randint(0, DATA_LENGTH)
  used = True
  while used:
    if DATA_LENGTH == len(positions_used):
      return 100 #Only for cheaters
    elif position in positions_used:
      position = random.randint(0, DATA_LENGTH)
    else:
      used = False
      positions_used.append(position)
      return position

def compare_followers(a_followers, b_followers,answer):
  if a_followers > b_followers:
    return "a"
  else:
    return "b"

playing = True
while playing:
  active_round = True
  score = 0
  while active_round:
    print(art.logo)
    if score < 1:
      primary = get_position()
    secondary = get_position()
    print("\nCompare A: " + get_info_data(primary))
    print(art.vs)
    print("Against B: " + get_info_data(secondary))
    primary_followers = get_followers(primary)
    secondary_followers = get_followers(secondary)
    correct_answer_type = False
    while not correct_answer_type:
      answer = input("\nWho was the most followers? A or B: ").lower()
      if answer == "a" or answer == "b":
        correct_answer_type = True
    
    result = compare_followers(primary_followers, secondary_followers,           answer)
    clear()
    if(result == answer):
      score += 1
      print(f"\nCorrect! Current score: {score}")
      primary = secondary
    else:
      print(art.logo)
      print("\nWrong!")
      score = 0
      active_round = False

  
  another_one = input("\nWant to try again [yes/no] : \n").lower()
  if another_one == "no":
    playing = False
    print("\nThanks for playing")
  else:
    positions_used = []
    active_round = True
  
  
