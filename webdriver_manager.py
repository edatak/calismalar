from selenium import webdriver
from webdriver_manager import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce_Demo:
    def empty_username_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(3)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(4)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(4)
        loginBtn.click()
        sleep(3)
        error_msg=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        testResult = error_msg.text == "Epic sadface: Username is required"
        print(testResult)
    
    def only_empty_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(3)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(3)
        loginBtn.click()
        sleep(3)
        error_msg=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        testResult = error_msg.text == "Epic sadface: Password is required"
        print(testResult)
    
    def locked_out_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        error_msg = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        testResult = error_msg.text == "Epic sadface: Sorry, this user has been locked out."
        print(testResult)

    def remove_error_msg(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorBtn=driver.find_element(By.CLASS_NAME, "error-button")
        errorBtn.click()
        print("Error Button")
    
    def go_to_inventory_page(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        redirectedPage="https://www.saucedemo.com/inventory.html"
        print(redirectedPage)
    
    def listOfItems(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        listOfItems=driver.find_elements(By.CLASS_NAME, "inventory_item")
        print("Number of Items: ",len(listOfItems))
        
testClass = Test_Sauce_Demo()
testClass.empty_username_password()
testClass.only_empty_password()
testClass.locked_out_user()
testClass.remove_error_msg()      
testClass.listOfItems() 