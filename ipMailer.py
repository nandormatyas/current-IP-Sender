import smtplib, ssl
import ipGetter
import fileController
import env
import schedule
import time
import datetime

period = input("How often would you like to check your ip in minutes? ")
print("Watching...")
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = env.os.environ['SENDER']
receiver_email = env.os.environ['RECEIEVER']
password = env.os.environ['PASS']

def mailer():

    message2 = ipGetter.ipGetter()

    if message2 :
        print("Ip changed, preparing email...")
        message = "Subject: {} \n\n Your IP has changed to {}".format("Your home server IP changed", message2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent")
            fileController.logCreator(str(datetime.datetime.now()), "Ip changed, email sent! \n New IP: {}".format(message2))
    else :
        fileController.logCreator(str(datetime.datetime.now()), "Ip has not changed since last check")
        print("Ip did not change")

schedule.every(int(period)).minutes.do(mailer)

while True:
    schedule.run_pending()
    time.sleep(1)