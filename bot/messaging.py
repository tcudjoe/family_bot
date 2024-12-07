from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = 'AC8155da86a73892dc17d5c91c95237ad8'
AUTH_TOKEN = 'f1a11a03fca08e390019fddf8afcd12c'
WHATSAPP_NUMBER = '+14155238886'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_msg(to, msg):
    client.messages.create(
        body=msg,
        from_=f'whatsapp:{WHATSAPP_NUMBER}',
        to=f'whatsapp:{to}'
    )