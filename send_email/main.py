import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "pass123"
subject = "Python email"
body = "This is the email"

message = f"""From: {sender} 
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
except smtplib.SMTPServerDisconnected:
    print("unable to sign in")
