from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC30f402f669bb8ae6882b6b5d64cab4eb"
# Your Auth Token from twilio.com/console
auth_token  = "910421966f0aac4e64b18829ec46ba2a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12502025606",
    from_="+12268871723",
    body="Hello from Python!",
    )

print(message.sid)
