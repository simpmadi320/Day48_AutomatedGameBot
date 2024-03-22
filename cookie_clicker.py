from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def get_upgrades(cookie_driver):
    all_buttons = cookie_driver.find_elements(By.CSS_SELECTOR, value="#store b")
    to_return = {}
    for n in range(len(all_buttons) - 1):
        text = all_buttons[n].text.split("-")
        to_return[n] = {"Clickable": all_buttons[n], "Item": text[0].strip(),
                       "Cost": int(text[1].strip().replace(",", ""))}
    return to_return

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

upgrades = get_upgrades(driver)

timeout = time.time() + 1
cookies = 0

while True:

    if time.time() > timeout:
        timeout = time.time() + 0.01a
        cookie.click()
        cookies += 1

        for upgrade_key in upgrades:
            upgrade = upgrades[upgrade_key]
            if cookies > upgrade["Cost"]:
                print("You can buy a " + upgrade["Item"] + " as you have " + str(cookies) + " cookies")
                cookies -= upgrade["Cost"]
                upgrade["Clickable"].click()
                upgrades = get_upgrades(driver)
