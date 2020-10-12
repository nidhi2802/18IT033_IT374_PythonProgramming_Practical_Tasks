from twilio.rest import Client
account_sid = '#################################'
auth_token = '################################'
client = Client(account_sid, auth_token)
message = client.messages.create(
from_='+1##########',
body ='Test SMS for sending message using Twilio and Python',
to ='+91##########'

)
print(message.sid)
