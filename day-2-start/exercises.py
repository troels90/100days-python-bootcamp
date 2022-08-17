# 2.1
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
new_num_digit_one = int(two_digit_number[0])
new_num_digit_two = int(two_digit_number[1])
new_str_digit = str(new_num_digit_one+new_num_digit_two)

print(new_str_digit)

####################################
#2.2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
bmi = float(weight) / float(height)**2
print(int(bmi)) 
#####################################
#2.3
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
days = (90-int(age))*365
weeks = (90-int(age))*52
months = (90-int(age))*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")




