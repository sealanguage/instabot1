from selenium import webdriver
from time import sleep
from pw import pw
import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()      #  this will encrypt the connection
smtpObj.ehlo()

#  login to server. email, generated
smtpObj.login('laneiodev@gmail.com', 'dfiqxsvqmichnkft')

# create an email to be sent automatically
subject = "This is email sent from instabot"
body = "Your color site data has been changed. Your new data is here"
msg = "Subject: {subject}\n\n\n {body}"

#  email to send
smtpObj.sendmail(
    "laneiodev@gmail.com",
    "efroehlich@cox.net",
    msg
)


# finish and clean up
smtpObj.quit()
print("email successfully sent")


# send email to user function
# def send_mail(self):
#     server = smtplib.SMTP('smtp.gmail.com', 587)    #  587
#     server.ehlo()
#     server.starttls()
#
#     # login to email account and use app password for authentication
#     server.login("elaneiodev@gmail.com", "dfiqxsvqmichnkft")
#
#     # create an email to send to confirm data change
#     subject = "igbot data working, sent"
#     body = 'Your color site data has been changed. Your new data is {new_pw}'
#     msg = "Subject: {subject}\n\n\n {body}"
#
#     # email to send from, email to send to, call the msg created above
#     server.sendmail(
#         'laneiodev@gmail.com',
#         'elaine.froehlich@gmail.com',
#         msg
#     )
#
#     # quit and print to the console that email was sent
#     server.quit()
#     print("Email has been successfully sent")


# send_mail()