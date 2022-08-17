# 3.1
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

########## 3.2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

bmi = int(round((weight / height**2), 0))
bmi_text = f"Your BMI is {bmi}, you are "
text_normal_weight = "have a "

if bmi < 25:
    if bmi > 20:
        print(bmi_text[:len(bmi_text)-4] + text_normal_weight + "normal weight.")
    elif bmi < 20:
        print(bmi_text + "underweight.")
elif bmi > 25:
    if bmi > 35:
        print(bmi_text + "clinically obese") 
    elif bmi > 30:
        print(bmi_text + "obese.")
    elif bmi < 30:
        print(bmi_text + "slightly overweight.")

####### 3.3
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
leap_year = "Leap year."
not_leap_year = "Not leap year."
bool_leap = False

if (year % 4) == 0:
    bool_leap = True
    if(year % 100) == 0:
        bool_leap = False
        if (year % 400) == 0:
            bool_leap = True

if(bool_leap == True):
    print(leap_year)
else:
    print(not_leap_year) 

###### 3.4
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
final_bill = 0

if size == "L":
    final_bill += 25
    if add_pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
elif size == "M":
    final_bill += 20
    if add_pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
elif size == "S":
    final_bill += 15
    if add_pepperoni == "Y":
        final_bill += 2
    if extra_cheese == "Y":
        final_bill += 1

print(f"Your final bill is: ${final_bill}.")

##### 3.5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
true_word = "true"
love_word = "love"
true_score = 0
love_score = 0
final_score = ""

for i in true_word:
    true_score += (name1.lower().count(i))
    true_score += (name2.lower().count(i))

for i in love_word:
    love_score += (name1.lower().count(i))
    love_score += (name2.lower().count(i))

final_score = str(true_score) + str(love_score)

score_text = "Your score is " + final_score

if(int(final_score) < 10 or int(final_score) > 90):
    print(score_text + ", you go together like coke and mentos.")
elif(int(final_score) > 40 and int(final_score) < 50):
    print(score_text + ", you are alright together.")
else:
    print(score_text + ".")