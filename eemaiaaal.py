import smtplib
import os
from email.message import EmailMessage
email_id = os.environ.get("EMAIL_USER") 
email_pass = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = 'Fight again Corona Virus'
msg['From'] = email_id
msg['To'] = 'Receiver Email Address'
msg.set_content("Hey, Hi let's fight against corona virus by staying at home")


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

  
    smtp.login(email_id,email_pass)

    smtp.send_message(msg)



