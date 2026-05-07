import os
from twilio.rest import Client 

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    
    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            to=os.getenv("TWILIO_VERIFIED_NUMBER")
        )

        print(message.sid)