import smtplib
import ssl
import os
from flask import current_app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(from_email: str, to_email: str, subject: str, content: str,
              is_html: bool) -> None:
    try:
        email_smtp = os.getenv('EMAIL_SMTP', '')
        email_port = os.getenv('EMAIL_PORT', '')
        email_login = os.getenv('EMAIL_LOGIN', '')
        email_password = os.getenv('EMAIL_PASSWORD', '')

        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        body = MIMEText(content, 'html' if is_html else 'plain')
        message.attach(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(email_smtp, int(email_port),
            context=context) as server:
            server.login(email_login, email_password)
            server.sendmail(from_email, to_email, message.as_string())
    except Exception as err:
        msg = 'Error to send e-mail: \n' + str(err)
        current_app.logger.error(msg)
