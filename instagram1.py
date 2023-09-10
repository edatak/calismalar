from selenium import webdriver
import time
from instagramUserInfo import username, password

url = "https://www.instagram.com/"

class Instagram:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome()
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.username = username
        self.password = password


def signIn(self):
   self.driver.get("https://www.instagram.com/accounts/login/")
   time.sleep(2)
   usernameInput= self.driver.find_element("xpath", "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(username)
   passwordInput= self.driver.find_element("xpath", "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)
   time.sleep(1)

   usernameInput.send_keys(username)
   passwordInput.send_keys(password)
   passwordInput.send_keys.ENTER
   time.sleep(2)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
time.sleep(2)



driver.find_element("xpath", "//*[@id='loginForm']/div/div[3]/button/div").click()
time.sleep(2)

driver.close()