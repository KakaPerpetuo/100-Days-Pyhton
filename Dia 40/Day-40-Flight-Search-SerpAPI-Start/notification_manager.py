import os
from twilio.rest import Client
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        #self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]

    # def send_sms(self, message_body):
    #     message = self.client.messages.create(
    #         from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
    #         body=message_body,
    #         to=os.environ["TWILIO_VERIFIED_NUMBER"]
    #     )
    #     # Prints if successfully sent.
    #     print(message.sid)

    
    def send_email(self, email_list, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for email in email_list:
                connection.sendmail(from_addr=self.email, to_addrs=email, msg=f"Subject:Low price alert!\n\n{email_body}".encode('utf-8'))

