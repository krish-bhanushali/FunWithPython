import smtplib
from email.message import EmailMessage


emailAddress = "your_email"
emailPassword = "your_password"

message = EmailMessage()
message['Subject'] = 'Lets GO and Contribute'
message['From'] = emailAddress
message['To'] = 'receiver_email'
message.set_content('Hacktober fest is comming lets get a cup of coffee')


#here if the user has turned on the html images then he will receive the html we embed in the multiline String
message.add_alternative("""
<html>
<p>Hello from this side</p>
</html>

""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    
    
    smtp.login(emailAddress,emailPassword)
    smtp.send_message(message)  