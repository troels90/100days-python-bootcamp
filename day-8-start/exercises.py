#### 8.1
import math
#Write your code below this line 👇
def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#### 8.2
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    #Check even - except 2
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
#### 8.3