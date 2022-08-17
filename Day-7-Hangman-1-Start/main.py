#Step 1
import random
import hangman_art
import hangman_words

word = random.choice(hangman_words.word_list)
player_lives = 6
used_letters = ""

display = []
for i in range(0, len(word)):
    display.append("_")

def end_game():
    if player_lives == 0:
        print(f"No mores lives! The word was {word.upper()} - you looooose!")
        return True
    elif display.count("_") > 0:
        return False
    else: 
        print(f"The word was {word.upper()} - CONGRATULATIONS")
        return True

print(hangman_art.logo + "\n \n")

while not end_game():  
    guess = input("Suggest a letter: ").lower()
    counter = 0
    word_count = 0
    for letter in word:
        if guess == letter:
            display[counter] = guess
            word_count += 1
        counter += 1
    if word_count > 0:
      print(f"There are {word_count} {guess}")
    else:
      player_lives -= 1
      print("No Matches")
    used_letters += guess
    print(f"{display}  |  Used Letters : {used_letters}")
    print(hangman_art.stages[player_lives])

