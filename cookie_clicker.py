from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

all_clickables = driver.find_elements(By.CSS_SELECTOR, value="#store b")

upgrades = {}
for n in range(len(all_clickables) - 1):
    text = all_clickables[n].text.split("-")
    upgrades[n] = {"Clickable": all_clickables[n], "Item": text[0].strip(), "Cost": int(text[1].strip().replace(",", ""))}

print(upgrades)

timeout = time.time() + 1
cookies = 0

while True:

    if time.time() > timeout:
        timeout = time.time() + 0.01
        cookie.click()
        cookies += 1

        for upgrade_key in upgrades:
            upgrade = upgrades[upgrade_key]
            if cookies > upgrade["Cost"]:
                print("You can buy a " + upgrade["Item"] + " as you have " + str(cookies) + " cookies")
                