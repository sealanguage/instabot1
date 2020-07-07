from selenium import webdriver
from time import sleep
from pw import pw
import smtplib


import os

# ask new password from the user
new_pw = input("Enter new password : ")
confirm_pw = input("Enter same password to confirm : ")


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

        # load un pw and submit login button
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(2)

        # click not now button
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)

        # click not now button notifications
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(2)

        # click to go to profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        sleep(4)


# change password
    def change_pw(self):
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        # sleep(2)

        # select the settings button
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
        sleep(2)

        # select change password button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/button[1]").click()
        sleep(2)

        # auto fill pw into pw input
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[1]/div/input").send_keys(pw)
        sleep(1)

        # ask user for new pw
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[2]/div/input").send_keys(new_pw)
        sleep(1)

        # ask user to confirm new pw
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[3]/div/input").send_keys(confirm_pw)
        sleep(1)

        # click change password button
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/div/button").click()
        sleep(2)

# send email to user function
#     def send_mail(self):
#         server = smtplib.SMTP('smtp.gmail.com', )
#         server.ehlo()
#         server.starttls()
#



if(new_pw == confirm_pw) :
    mybot = InstaBot('laneiodev', pw)
    mybot.change_pw()
else :
    print("Your passwords do not match!")

# if __name__ == "__main__" :
#     ig_bot = instagramBot("temp_username", "temp_password")

     # print(ig_bot.username)



