alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction):
    end_text = ""
    len_alphabet = len(alphabet)
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_pos = position + shift_amount
        if new_pos > len_alphabet and direction == "encode":
          new_pos = new_pos - len_alphabet
        if new_pos < 0 and direction == "decode":
          new_pos = new_pos + len_alphabet
        new_letter = alphabet[new_pos]
        end_text += new_letter
      else:
        end_text += letter    
    print(f"{direction} - {end_text}")

should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  another_one = input( "\n Would you like to go again? (yes/no)").lower()
  print(another_one)
  if another_one == "no":
    should_continue = False
    print("Goodbye!")

