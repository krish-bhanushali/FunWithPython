import smtplib
from email.message import EmailMessage


emailAddress = "your_email"
emailPassword = "your_password"

message = EmailMessage()
message['Subject'] = 'Lets GO and Contribute'
message['From'] = emailAddress
message['To'] = 'receiver_email'
message.set_content('Hacktober fest is comming lets get a cup of coffee')


#path to pdf mine is currently in the same directory hence I have only used the name
files = ['dummy.pdf']

#As in the multipleImageEmail.py one can also write a loop to have multiple pdf attachments

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        
      
        file_name = f.name

    message.add_attachment(file_data, maintype='application' , subtype='octet-stream' , filename=file_name)    


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    
    smtp.login(emailAddress,emailPassword)
    smtp.send_message(message)  