from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.nytimes.com/games/wordle/index.html"

driver = webdriver.Firefox()
driver.get(url)
title = driver.title
wait = WebDriverWait(driver, timeout=10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "fides-reject-all-button")))
cookie_button = driver.find_element(by=By.CLASS_NAME, value="fides-reject-all-button")
print(cookie_button)
play_button = driver.find_element(by=By.CLASS_NAME, value="Welcome-module_button__ZG0Zh:nth-child(3)")
print(play_button)

cookie_button.click()
driver.implicitly_wait(0.5)
play_button.click()

wait = WebDriverWait(driver, timeout=10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")))
close_button = driver.find_element(by=By.CLASS_NAME, value="Modal-module_closeIcon__TcEKb")
print(close_button)
close_button.click()

for x in "penis↵":
    button = driver.find_element(By.CSS_SELECTOR, f'[data-key="{x}"]').click()

sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
penis_dict = dict()
for x in soup.find_all("div"):
    if x.get("aria-live") == "polite":
        val = x.get("data-state")
        letter = x.get("aria-label")
        print(f"{letter[12]}: {val}")
        penis_dict[letter[12]] = val
print(penis_dict)
driver.quit()
return penis_dict
