from selenium import webdriver
from time import sleep
from pw import pw
import smtplib


# import os

# ask new instagram password from the user
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
        sleep(1)

        # click to go to profile
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        sleep(2)


# change password
    def change_pw(self):
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        # sleep(2)

        # select the settings button
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
        sleep(4)

        # select change password button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/button[1]").click()
        sleep(4)

        # auto fill pw into pw input
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[1]/div/input").send_keys(pw)
        sleep(4)

        # ask user for new pw
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[2]/div/input").send_keys(new_pw)
        sleep(4)

        # ask user to confirm new pw
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[3]/div/input").send_keys(confirm_pw)
        sleep(4)

        # click change password button
        #   driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(1); replace with py code
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/div/button").click()
        sleep(4)

#   driver management code from Joe
#   driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(1);
    #  try to use wait until you find this element and then continue on with the script
    #  specific wait   driver time span    wait until expected conditions    element by


# send email to user function
    print("Starting to send email")
    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)    #  587
        server.ehlo()
        server.starttls()
        server.ehlo()

        # login to email account and use app password for authentication
        server.login("laneiodev@gmail.com", "dfiqxsvqmichnkft")

        # create an email to send to confirm data change
        subject = "igbot data working, sent"
        body = 'Your color site data has been changed. Your new data is {new_pw}'
        msg = "Subject: {subject}\n\n\n {body}"

        # email to send from, email to send to, call the msg created above
        server.sendmail(
            'laneiodev@gmail.com',
            'elaine.froehlich@gmail.com',
            msg
        )

        # quit and print to the console that email was sent
        server.quit()
        print("Email has been successfully sent")

# validation to send un and pw, change pw and confirm pw change or print unmatched pws
if(new_pw == confirm_pw):
    mybot = InstaBot('laneiodev', pw)
    mybot.change_pw()
    mybot.send_mail()
else:
    print("Your passwords do not match!")






# ChromeOptions options = new ChromeOptions();
#             options.AddArgument("--headless");
#             //options.AddArgument("--remote-debugging-port=9222");
#             IWebDriver driver = new ChromeDriver(options); 
