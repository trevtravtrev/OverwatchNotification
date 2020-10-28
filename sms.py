import smtplib
import ssl


class SMS:
    def __init__(self, number, phone_carrier, username, password):
        self.CARRIERS = {
            'att': '@mms.att.net',
            'tmobile': '@tmomail.net',
            'verizon': '@vtext.com',
            'sprint': '@messaging.sprintpcs.com',
            'virgin': '@vmobl.com',
            'boost': '@smsmyboostmobile.com',
            'cricket': '@sms.cricketwireless.net',
            'metro': '@mymetropcs.com',
            'us cellular': '@email.uscc.net',
            'xfinity': '@vtext.com'
        }
        self.EMAIL_DOMAIN = 'smtp.gmail.com'
        self.EMAIL_PORT = 587

        self.receiver_email = f'{number}{self.CARRIERS.get(phone_carrier)}'
        self.username = username
        self.password = password

        self.initialize_server()

    def initialize_server(self):
        context = ssl.create_default_context()

        try:
            self.server = smtplib.SMTP(self.EMAIL_DOMAIN, self.EMAIL_PORT)
            self.server.ehlo()
            self.server.starttls(context=context)
            self.server.ehlo()
            self.server.login(self.username, self.password)

        except smtplib.SMTPException as exc:
            print(f'initialize_server error: {exc}')

    def send(self, message):
        try:
            self.server.sendmail(self.username, self.receiver_email, message)

        except Exception as e:
            print(f'send error: {e}')
