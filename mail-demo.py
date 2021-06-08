import os
import smtplib
from dotenv import load_dotenv
# import imghdr
from email.message import EmailMessage


load_dotenv()

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['bliotti@icloud.com', 'xxxx@xxxxx.io']

if EMAIL_PASSWORD is None:
    print("None")
elif EMAIL_ADDRESS is None:
    print("None")
else:
    msg = EmailMessage()
    msg['Subject'] = 'test subject'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(contacts)

    msg.set_content('plain text')

    msg.add_alternative("""\
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="color:SlateGray">This is HTML</h1>
</body>
</html>
                        """, subtype='html')

    # files = ['btccheat.png', 'me-jrs.jpg']
    # files = ['resume.pdf']

    # for file in files:
    #     with open(file, 'rb') as f:
    #         file_data = f.read()
    #         # file_type = imghdr.what(f.name)
    #         file_name = f.name

    #     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # with smtplib.SMTP('localhost', 1025) as smtp:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
