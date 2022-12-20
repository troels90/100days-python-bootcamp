import datetime as dt
import smtplib as smtp
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as file:
        quotes = file.readlines()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = weekdays[weekday]
    chosen_quote = random.choice(quotes)

    my_email = "troelstesting@hotmail.com"
    password = "abctest123"
    to_email = "trylletroels1602@gmail.com"

    with smtp.SMTP("smtp.office365.com") as connection:
        # Encrypt using TLS
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:{day}\n\n{chosen_quote}"
        )

