from selenium import webdriver
import time

url = "https://www.instagram.com/"

username = "usertest"
password = "test123*"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
time.sleep(10)

driver.find_element("xpath", "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(username)
driver.find_element("xpath", "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)
time.sleep(1)

driver.find_element("xpath", "//*[@id='loginForm']/div/div[3]/button/div").click()
time.sleep(10)

driver.close()