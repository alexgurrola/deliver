import smtplib
from email.mime.text import MIMEText


def push():
    from pyfcm import FCMNotification
    # Your api-key can be retrieved from:
    # https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
    push_service = FCMNotification(api_key="<api key>")
    registration_id = "<device registration_id>"
    message_title = "Uber update"
    message_body = "Hi john, your customized news for today is ready"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
    print(result)


def send():
    msg = MIMEText('Hello World!\n')
    msg['Subject'] = 'Just wanted to say hello!'
    msg['From'] = 'alex@sitetheory.io'
    msg['To'] = '9257659457@vtext.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    import plac
    try:
        plac.call(send)
    except KeyboardInterrupt:
        print('\nGoodbye!')
