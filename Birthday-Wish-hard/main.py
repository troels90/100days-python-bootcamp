##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib as smtp
import pandas

MY_EMAIL = "troelstesting@hotmail.com"
MY_PASSWORD = "abctest123"
FILEPATH = "letter_templates/"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
now = dt.datetime.now()
month = now.month
day = now.day
year = now.year
print(f"{month}  day: {day}")

data = pandas.read_csv("birthdays.csv")
birthday_people = {row[0]: row.email for (index, row) in data.iterrows() if day == row.day and month == row.month}
num_of_birthdays = len(birthday_people)

def birthday_wishes(name, email):
    random_letter = random.choice(LETTERS)
    url = FILEPATH + random_letter

    with open(url) as file_letter:
        letter_txt = file_letter.read()
        new_letter = letter_txt.replace("[NAME]", name)

    send_wishes(new_letter, email)


def send_wishes(letter, to_email):
    with smtp.SMTP("smtp.office365.com") as connection:
        # Encrypt using TLS
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday!\n\n{letter}")


for i in birthday_people:
    name = i
    email = birthday_people[i]
    birthday_wishes(name, email)

