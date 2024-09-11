import datetime
import wordle

def check_time():
    datetime_now = datetime.datetime.now()
    str_date = str(datetime_now.date())

    with open("last_wordle", "r") as f:
        date = f.readline()
    if date < str_date:
        return update_time(str_date)
    else:
        with open("score_wordle", "r") as f:
            score = f.readline()
            return score

def update_time(str_date):
    with open("last_wordle", "w") as f:
        f.write(str_date)
    return update_wordle()

def update_wordle():
    score = wordle.play_wordle()
    return(score)

