import os
from selenium import webdriver
from selenium.webdriver.common.by import By

if not os.path.isdir("pics"):
    os.mkdir("pics")

driver = webdriver.Firefox()
driver.get("https://store.epicgames.com/en-US/free-games")
driver.implicitly_wait(5)

games = driver.find_element(By.CLASS_NAME, "css-2u323")
driver.execute_script("arguments[0].scrollIntoView(true);", games)
driver.implicitly_wait(5)

driver.find_element(By.ID, "onetrust-reject-all-handler").click()
driver.implicitly_wait(5)
games.screenshot("./pics/test.png")

driver.quit()
