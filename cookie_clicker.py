from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

def Get_Clickables():
    all_buttons = driver.find_elements(By.CSS_SELECTOR, value="#store b")

    cookie_upgrades = {}
    for n in range(len(all_buttons) - 1):
        text = all_buttons[n].text.split("-")
        cookie_upgrades[n] = {"Clickable": all_buttons[n], "Item": text[0].strip(),
                              "Cost": int(text[1].strip().replace(",", ""))}
    return cookie_upgrades

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 1
cookies = 0

while True:

    if time.time() > timeout:
        timeout = time.time() + 0.01
        cookie.click()
        cookies += 1

        try:
            upgrades = Get_Clickables()
        except StaleElementReferenceException:
            continue

        for upgrade_key in upgrades:
            upgrade = upgrades[upgrade_key]
            try:
                if cookies > upgrade["Cost"]:
                    print("You can buy a " + upgrade["Item"] + " as you have " + str(cookies) + " cookies")
                    upgrade["Clickable"].click()
            except StaleElementReferenceException:
                continue
