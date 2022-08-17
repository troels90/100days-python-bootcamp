#### 5.1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_of_heights = 0
number_of_heights = len(student_heights)

for heights in range(0,number_of_heights):
    sum_of_heights += student_heights[heights]

avg_height = round((sum_of_heights / number_of_heights))
print(avg_height)

#### 5.2
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
cur_highscore = 0;

for score in student_scores:
    if score > cur_highscore:
        cur_highscore = score


print(f"The highest score in the class is: {cur_highscore}")

#### 5.3
#Write your code below this row 👇
sum_evens = 0
for number in range(1, 101):
    if(number % 2 == 0):
        sum_evens += number

print(sum_evens)

#### 5.4 FizzBuzz
#Write your code below this row 👇
fizz = False
buzz = False
fizzbuzz = False
fizz_str = "Fizz"
buzz_str = "Buzz"
for num in range(1,101):
    if(num % 3 == 0):
        fizz = True
    if(num % 5 == 0):
        buzz = True
    if(fizz == True and buzz == False):
        print(fizz_str)
        fizz = False
    elif(fizz == False and buzz == True):
        print(buzz_str)
        buzz = False
    elif(fizz == True and buzz == True):
        print(fizz_str+buzz_str)
        fizz = False
        buzz = False
    else:
        print(num)
