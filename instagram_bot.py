from selenium import webdriver
from time import sleep
from pw import pw

import os

class InstaBot :

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.instagram.com/')
        sleep(2)

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(4)


InstaBot('laneiodev', pw)

# if __name__ == "__main__" :
#     ig_bot = instagramBot("temp_username", "temp_password")

     # print(ig_bot.username)
