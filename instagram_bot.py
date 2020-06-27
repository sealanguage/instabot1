from selenium import webdriver
from time import sleep
from pw import pw

import os

class InstaBot :

    def __init__(self, username, pw):
        """
            initializes an instance of the InstaBot class
            Args:
                username: str: the instagram user name for a user
                pw: str: the instagram password for a user
            Attributes:
                driver: selenium web driver. Chrome: the chromedriver that is used to automate browser actions


        """
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.instagram.com/')
        sleep(2)

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(2)

        # self.driver.find_element_by_name('$0').click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        sleep(4)


# change password
    def change_pw(self):
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        # sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
        sleep(2)

mybot = InstaBot('laneiodev', pw)
mybot.change_pw()

# if __name__ == "__main__" :
#     ig_bot = instagramBot("temp_username", "temp_password")

     # print(ig_bot.username)



