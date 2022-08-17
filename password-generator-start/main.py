#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
str_letters = ""
str_symbols = ""
str_numbers = ""
letter_len = int(len(letters))-1
symbol_len = int(len(symbols))-1
number_len = int(len(numbers))-1
password_list = []

for i in range (0, nr_letters):
  letter_place = random.randint(0,letter_len)
  password_list.append(letters[letter_place])

for i in range (0, nr_symbols):
  symbol_place = random.randint(0, symbol_len)
  password_list.append(symbols[symbol_place])

for i in range (0, nr_numbers):
  number_place = random.randint(0,number_len)
  password_list.append(numbers[number_place])

###Randomize Look
password_size = int(len(password_list))
password_str = ""

for x in range (0, password_size):
  flex_size = int(len(password_list))-1
  position = random.randint(0, flex_size)
  password_str += password_list[position]
  password_list.pop(position)

print(password_str)