import datetime

datetime_now = datetime.datetime.now()
str_date = str(datetime_now.date())
outdated = False

with open("last_wordle", "r") as f:
    for date in f:
        print(date)
        if date < str_date:
            outdated = True

if outdated is True:
    with open("last_wordle", "w") as f:
        f.write(str_date)
