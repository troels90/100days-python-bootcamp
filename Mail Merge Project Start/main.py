#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()

with open("input/Letters/starting_letter.txt") as file_letter:
    letter_txt = file_letter.read()

NEW_FILE_FORMAT = ".txt"

def create_letter(position):
    name = format_names(position)
    final_txt = letter_txt.replace("[name]", name)
    with open("Output/ReadyToSend/letter_for_"+name+NEW_FILE_FORMAT, mode="w") as file:
        file.write(final_txt)

def format_names(position):
    new_name = ""
    if names[position].find("\n") > 0:
        new_name = names[position][:-1]
        print(new_name)
    else:
        new_name = names[position]
        print(new_name)
    return new_name

for i in range(0,len(names)):
    create_letter(i)

