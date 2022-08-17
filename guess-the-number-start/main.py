import art
import random
print(art.logo)
#Number Guessing Game Objectives:
number = random.randint(1,101)
lives = 10
guessed = False
difficult = input("Easy or Hard: ").lower()
if difficult == "hard":
  lives = 5
  
while not guessed:
  if lives == 0:
    guessed = True #But not really
    print("No more lives :(")
  else:
    print(f"You have {lives} attempts remaining")
    guess_input = int(input("Make a guess: "))
    if guess_input == number:
      guessed = True
      print(f"{number} is the right number!")
    elif guess_input < number: 
      print("Too low")
      lives -= 1
    elif guess_input > number:
      print("Too high")
      lives -= 1
  
  
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

