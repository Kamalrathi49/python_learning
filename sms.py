from twilio.rest import Client

account_sid = 'AC23c735c5f65258837a9e32d4945e68d0'
auth_token = '0748e768af5ed92bc33935ce291a30ed'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG945ef48934ee3dbe696cdc728bc399fc',
    body='testing sms in python --by Kamal Rathi',
    to='+918059910473'
)

print(message.sid)
