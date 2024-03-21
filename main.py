from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

"""
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.ca/Hornet-Watersports-Dragon-Boat-Paddle/dp/B0C28ZH8VH/ref=sr_1_13?crid=1AE5ZEQZUQQIZ&dib=eyJ2IjoiMSJ9.UPy4a451FcpUIpK7dL4yAF56rzairLI1bzsiPGLvjhuqeat1SZv4sADc-D7QlqAZhoZ65OSbkC38pdpmHE-PBpD1Z6X8vM1Il-J-CtaQBxAeQUZwxwsYo1v9N7rtGHm1RwiPPZONDUY3Ojq0ESftWW5tX_YdIYHlgfGG9WKp84UKEjjgL_p1K9KrWY7s6X3BvZ5fvubsiAYA7hFg3ZPW9IXbXnQZZjD4NtKGx472uCWR6A1iBXXAtnXz6TRCWKpVwXGh4blzpfG1pLm54f9IFuCaL5WdqZxQ303T_x2FayY.QfjxJjj02v83oufFgRIXamdUa2JUZmt0Of2x7uvd3eI&dib_tag=se&keywords=dragon%2Bboat%2Bpaddle&qid=1710974241&sprefix=dragon%2Bboat%2Bpaddle%2Caps%2C101&sr=8-13&th=1&psc=1")
dollar_cost = driver.find_element(By.CLASS_NAME, "a-price-whole").text
cent_cost = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
cost = f"{dollar_cost}.{cent_cost}"
print("The price is " + cost)
"""

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(names)):
    events[n] = {
        "time": dates[n].text,
        "name": names[n].text
    }

print(events)
driver.quit()

