from selenium import webdriver
import os
import time

class instagramBot :

    def __init__(self, username, password) :
        self.username = username
        self.password = password

if __name__ == "__main__" :
    ig_bot = instagramBot("temp_username", "temp_password")

    print(ig_bot.username)
