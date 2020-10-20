# coding: utf-8

import smtplib
from email.message import EmailMessage
from .celery import app
from utils import get_app_config

@app.task
def send_email(recipient, subject, message):
    app_config = get_app_config()
    server = smtplib.SMTP(app_config['host'], app_config['port'])

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = app_config['sender']
    msg['To'] = recipient

    try:
        server.login(app_config['sender'], app_config['password'])
        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()
