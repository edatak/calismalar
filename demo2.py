from selenium import webdriver

browser = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from instagramUserInfo import username, password
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
import time

class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(service= service, options= options)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element("xpath", "//*[@id='loginForm']/div/div[1]/div")
        passwordInput = self.browser.find_element("xpath", "//*[@id='loginForm']/div/div[2]/div")

        usernameInput.send_keys(str(self,username))
        passwordInput.send_keys(self,password)
        time.sleep(2)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_elemet_by_xpath("//*[@id='mount_0_0_m4']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        time.sleep(2)

        dialog= self.browser.find_element_by_css_selector("div[role=dialog ul")
        followerCount = len(dialog.find_element_by_css_selector("li"))
        
        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            time.sleep(2)

            newCount= len(dialog.find_element_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second Count: {newCount}")
                time.sleep(1)
            else:
                break
              
        followers= dialog.find_element_by_css_selector("li")
        
        followerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)

        with open("followers.txt", "w", encoding= "UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def follewUser(self,username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButon = self.browser.find_element_by_tag_name("button")
        if followButon.text != "Following":
            followButon.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unFollowUser(self,usename):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "following":
            followButton.click()
            time.sleep(2)
            self.broser.find_element_by_xpath('//button[text()= "UnFollow]').click()
        else:
            print("Zaten takip etmiyorsunuz.")


instgrm = Instagram(username,password)
instgrm.signIn()
instgrm.getFollowers()
#instgrm.follewUser('kod_evreni')
#instgrm.unFollowUser("kod_evreni")

# list= ["kod_evreni", ""]

# for user in list:
#     instgrm.follewUser(user)
#     time.sleep(3)