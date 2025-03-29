import smtplib
import os
email_id = os.environ.get("EMAIL_USER") 
email_pass = os.environ.get("EMAIL_PASS")
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    # ehlo is an alternative to helo for services that support the smtp services extenstions

    smtp.login(email_id,email_pass)

    subject = 'Fight again Corona Virus'
    body = "Hey, Hi let's fight against corona virus by staying at home"

    msg = f'Subject:{subject}\n\n\n{body}'
    smtp.sendmail(email_id,'#Receiver Email Address',msg)

    # format here is senders email id  --- receivers email id, =--- msg


