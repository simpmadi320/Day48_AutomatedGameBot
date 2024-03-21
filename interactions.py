from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "search")))
search.send_keys("Python")
search.send_keys(Keys.RETURN)
