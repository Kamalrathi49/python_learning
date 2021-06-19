from twilio.rest import Client

account_sid = 'account sid'
auth_token = '[]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG945ef48934ee3dbe696cdc728bc399fc',
    body='testing sms in python --by Kamal Rathi',
    to='mobile number'
)

print(message.sid)
