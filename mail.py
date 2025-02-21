from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText


smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_username = 'nothingevergoesplanned@gmail.com'
email_password = 'dxwp jkdu uqmo velb'

email = 'ramh3637@gmail.com'
booking_number = '9876'

 # Send Email using SMTP
msg = MIMEMultipart()
msg['From'] = email_username
msg['To'] = email
msg['Subject'] = 'OT Booking Successful'
body = f"Your OT booking (number: {booking_number}) was successful!"
msg.attach(MIMEText(body, 'plain'))
        
print('test2')

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_username, email_password)
text = msg.as_string()
server.sendmail(email_username, email, text)
server.quit()
print('success')
        
