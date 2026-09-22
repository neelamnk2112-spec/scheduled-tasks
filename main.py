import smtplib
import csv
import datetime as dt
import random

today=dt.date.today()
EMAIL_ADDRESS = "sonali.creator713@gmail.com"
PASSWORD = "pmjv cqnd ztos hywd"

letter = random.randint(1, 3)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    with open("birthdays.csv") as csvfile:
        birthdays = csv.DictReader(csvfile)

        for birthday in birthdays:
            birth_month=int(birthday["month"])
            birth_day=int(birthday["day"])

            if birth_month==today.month and birth_day==today.day:

                with open(f"./letter_templates/letter_{letter}.txt","r") as file:
                    data=file.read()
                    new_data=data.replace("[NAME]",birthday["name"])
                    new_data=new_data.replace("Angela","Sonali")
                smtp.sendmail(EMAIL_ADDRESS, birthday["email"], msg=f"Subject:Happy Birthday!\n\n{new_data}")


