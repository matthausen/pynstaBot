from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

class pynstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def unfollow(self):
        
        driver = self.driver
        driver.get("https://www.instagram.com/hello_lingua/")
        time.sleep(2)

        driver.find_element_by_xpath("//a[contains(., 'following')]").click()
        time.sleep(2)
        following_list = driver.find_elements_by_class_name("FPmhX")
        for following in following_list:
            try:
                following.click()
                time.sleep(2)
                following_followers = driver.find_elements_by_class_name("g47SY")[1]
                x = following_followers.get_attribute("title")
                y = int(x)
                if y > 1000:
                    print("keep follower")
                else:
                    print("unfollow")

                    #To continue

            except Exception as e:
                time.sleep(2)
                
        
        

if __name__ == "__main__":

    username = "youremail"
    password = "yourpassword"

    ig = pynstaBot(username, password)
    ig.login()

    while True:
        try:
            ig.unfollow()
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = pynstaBot(username, password)
ig.login()