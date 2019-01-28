import smtplib, ssl
import ipGetter
import env

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = env.os.environ['SENDER']
receiver_email = env.os.environ['RECEIEVER']
password = env.os.environ['PASS']
message2 = ipGetter.ipGetter()
message = """\
Subject: Your home server IP changed

Your IP has changed to {}""".format(message2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
