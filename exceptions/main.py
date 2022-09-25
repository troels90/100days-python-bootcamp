
try:
    file = open("data.txt")
    a_dict = {"key":"value"}
    a_dict["key"]
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("File created - HELLO")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else: #Only runs if 'try-block' has no except-ions
    content = file.read()
    print(content)
finally: #Runs no matter what
    file.close()
    print("File closed")

# BMI calculator - create exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters!")

bmi = weight / height ** 2
print(bmi)

# 30.1 Fruit pies and exception
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(2)

# 30.2 KeyError in for loop

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)