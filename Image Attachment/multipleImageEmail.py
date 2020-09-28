import smtplib
from email.message import EmailMessage
# inbuilt library to get image type
import imghdr

emailAddress = "your_email"
emailPassword = "your_password"

message = EmailMessage()
message['Subject'] = 'Lets GO and Contribute'
message['From'] = emailAddress
message['To'] = 'receiver_email'
message.set_content('Hacktober fest is comming lets get a cup of coffee')


#mention path to photo here , since mine is already where the file is I have written the name of the file
files = ['hacktoberfest.jpg','hacktoberfest1.png','hacktoberfest2.jpeg']

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        # to identify file type
        file_type = imghdr.what(f.name)
        file_name = f.name

    message.add_attachment(file_data, maintype='image' , subtype=file_type , filename=file_name)    


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    
    smtp.login(emailAddress,emailPassword)
    smtp.send_message(message)