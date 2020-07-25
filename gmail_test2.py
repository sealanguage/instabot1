import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = 'Check this out Im sending automatically'
msg['From'] = EMAIL_ADDRESS
msg['TO'] = "efroehlich@cox.net"
msg.set_content('putImageNameHere')

# with open ('image_path.jpg', 'rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)