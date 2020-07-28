import smtplib, ssl


def read_creds():
    # user = passw = " "
    with open("creds.txt", "r") as f:
        file = f.readlines()
        # print(file)    #  this did print the text file successfully
        user = file[0].strip()
        passw = file[1].strip()
        return user, passw


user: str
user, passw = read_creds()
reciever = "efroehlilch@cox.net"
port = 456


print(user, passw)        #  successfully gets user and password from text file

# sender = "laneiodev@gmail.com"
# passw = "dfiqxsvqmichnkft"


msg = """\
    Subject: Python email 3.
    This is from Python
    from laneiodev
"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(user, passw)
    server.sendmail(user, reciever, msg)
print("message sent")