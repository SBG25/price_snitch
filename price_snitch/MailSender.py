import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSender:
    subject = "Aviso de precios"

    def __init__(self, sender, password, receiver):
        self.sender = sender
        self.password = password
        self.receiver = receiver

    def send_mail(self, msg):
        mail_content = msg

        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = self.subject
        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.sender, self.password)

        text = message.as_string()
        session.sendmail(self.sender, self.receiver, text)
        session.quit()
