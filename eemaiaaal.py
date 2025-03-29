import smtplib
import os
import imghdr
from email.message import EmailMessage
email_id = os.environ.get("EMAIL_USER") 
email_pass = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = 'Check out these images'
msg['From'] = email_id
msg['To'] = 'Receiver Email'
msg.set_content("Image has been Attached !!")

#files = ['Hello.jpg','Hello1.jpg']
files = ['Testing.pdf']

for file in files:

    with open(file,'rb') as m:
       file_data = m.read()
       #file_type = imghdr.what(m.name)
       file_name = m.name
       #print(file_type)

    #msg.add_attachment(file_data, maintype = 'image', subtype = file_type,filename = file_name)
    msg.add_attachment(file_data, maintype = 'image', subtype = 'octet-stream',filename = file_name)



with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

  
    smtp.login(email_id,email_pass)

    smtp.send_message(msg)



