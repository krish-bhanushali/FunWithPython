import smtplib


emailAddress = "your_email"
emailPassword = "your_password"

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(emailAddress,emailPassword)

    subject = 'Lets Go and Contribute'
    body = 'Open source is fun, lets get a cup of coffee'
    message = f'Subject : {subject}\n\n{body}'

    smtp.sendmail(emailAddress,'receiver_email',message)



