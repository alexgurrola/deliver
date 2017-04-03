from twilio.rest import TwilioRestClient

# connect
credentials = {
    "sid": "",
    "token": "",
}
client = TwilioRestClient(credentials['sid'], credentials['token'])

# send
settings = {
    "body": "Hello World!",
    "to": "+12345678901",
    "from_": "+12345678901"
}
message = client.messages.create(**settings)

# output
print(message.sid)
