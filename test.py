from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcb73e44e38653e08f174446161e4c276"
# Your Auth Token from twilio.com/console
auth_token  = "6f60d9fffbac16025702d41d4d0f37b4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12132928296", 
    from_="+15412142354",
    body="OBTU")

print(message.sid)