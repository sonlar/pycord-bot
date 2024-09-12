import datetime
import json
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot():
    driver = webdriver.Firefox()
    driver.get("https://store.epicgames.com/en-US/free-games")
    driver.implicitly_wait(5)
    
    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.visibility_of_element_located((By.ID, "onetrust-reject-all-handler")))
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()


    games = driver.find_element(By.CLASS_NAME, "css-2u323")
    driver.execute_script("arguments[0].scrollIntoView(true);", games)
    driver.implicitly_wait(5) 

    driver.implicitly_wait(5)
    games.screenshot("./pics/test.png")
    
    driver.implicitly_wait(5)
    date = driver.find_element(By.TAG_NAME, "time").get_attribute("datetime")

    driver.quit()
    return date

def has_expired():
    print("in has_expired")
    with open("data.json", "r") as f:
        data = json.load(f)
    current_date = datetime.datetime.now(datetime.timezone.utc)
    current_timestamp = current_date.isoformat()
    epic_timestamp = data["epic"]["timestamp"]

    if epic_timestamp < current_timestamp:
        print("in epic < current")
        try:
            data["epic"]["timestamp"] = take_screenshot()
            split_timestamp = [date for date in re.split("-|T|:", data["epic"]["timestamp"])]
            split_timestamp = split_timestamp[:5]
            split_timestamp = [int(date) for date in split_timestamp]
            split_timestamp[3] += 2

            epoch_timestamp = datetime.datetime(split_timestamp[0], split_timestamp[1], split_timestamp[2], split_timestamp[3], split_timestamp[4]).timestamp()
            data["epic"]["discord_timestamp"] = int(epoch_timestamp)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
            return True, int(epoch_timestamp)
        except TimeoutException:
            print("timed out, probably anti-bot")
 
    print("in epic > current")
    return False, 0

