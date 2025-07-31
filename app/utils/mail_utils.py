from flask import current_app
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import config


def send_mail(from_mail: str, to_mail: str, subject: str, message: str,
              is_html: bool) -> None:
    """
    Send email using the config parameters
    """
    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = from_mail
        message['To'] = to_mail
        message['Subject'] = subject
        body = MIMEText(message, 'html' if is_html else 'plain')
        message.attach(body)

        # Send email
        context = ssl.create_default_context()
        if config['mail_ssl']:
            with smtplib.SMTP_SSL(
                    config['mail_smtp'],
                    config['mail_port'],
                    context=context) as server:
                server.login(config['mail_login'], config['mail_password'])
                server.sendmail(from_mail, to_mail, message.as_string())
        else:
            server = smtplib.SMTP(config['mail_smtp'], config['mail_port'])
            server.starttls(context=context)
            server.login(config['mail_login'], config['mail_password'])
            server.sendmail(from_mail, to_mail, message.as_string())
    except Exception as err:
        msg = 'Error to send e-mail: \n' + str(err)
        current_app.logger.error(msg)


def send_html_mail(from_mail: str, to_mail: str, subject: str,
                   message: str) -> None:
    """
    Wrapper to send_mail(..., html=True)
    """
    send_mail(from_mail, to_mail, subject, message, True)


def send_text_mail(from_mail: str, to_mail: str, subject: str,
                   message: str) -> None:
    """
    Wrapper to send_mail(..., html=False)
    """
    send_mail(from_mail, to_mail, subject, message, False)
