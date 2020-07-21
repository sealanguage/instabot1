import smtplib

# smtpObj = smtplib.SMTP('smtp,gmeil.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
#
# #  login to server. email, generated
# smtpObj.login('efroehlich@g.rwu.edu', )

# send email to user function
    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)    #  587
        server.ehlo()
        server.starttls()

        # login to email account and use app password for authentication
        server.login("elaneiodev@gmail.com", "dfiqxsvqmichnkft")

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


send_mail()