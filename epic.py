import check
import datetime
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def take_screenshot():
    driver = webdriver.Firefox()
    driver.get("https://store.epicgames.com/en-US/free-games")
    driver.implicitly_wait(5)

    games = driver.find_element(By.CLASS_NAME, "css-2u323")
    driver.execute_script("arguments[0].scrollIntoView(true);", games)
    driver.implicitly_wait(5)

    driver.find_element(By.ID, "onetrust-reject-all-handler").click()
    driver.implicitly_wait(5)
    games.screenshot("./pics/test.png")
    
    driver.implicitly_wait(2)
    date = driver.find_element(By.TAG_NAME, "time").get_attribute("datetime")

    driver.quit()
    return date

def has_expired():
    check
    with open("data.json", "r") as f:
        data = json.load(f)
    current_date = datetime.datetime.now(datetime.timezone.utc)
    current_timestamp = current_date.isoformat()
    epic_timestamp = data["epic"]["timestamp"]

    if epic_timestamp < current_timestamp:
        data["epic"]["timestamp"] = take_screenshot()

        split_timestamp = [date for date in re.split("-|T|:", data["epic"]["timestamp"])]
        split_timestamp = split_timestamp[:5]
        split_timestamp = [int(date) for date in split_timestamp]

        epoch_timestamp = datetime.datetime(split_timestamp[0], split_timestamp[1], split_timestamp[2], split_timestamp[3], split_timestamp[4]).timestamp()
        data["epic"]["discord_timestamp"] = epoch_timestamp

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

