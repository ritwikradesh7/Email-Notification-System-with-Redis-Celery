#Importing celery for job queue & smptlib for sending emails, os for environment variables
from celery import Celery
import smtplib
import os

#initializing the Celery app with Redis as the message broker
#tasks is name of the app, broker specifies where the tasks will be queued
celery = Celery('tasks', broker='redis://redis:6379/0')

#Celery task to send an email
@celery.task
def send_email_task(to, subject, body):
    try:
        #Fetching SMTP server credentials from env
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = int(os.getenv('SMTP_PORT'))   
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')

        message = f"Subject: {subject}\n\n{body}"

        #Connecting to the SMTP server and sending the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to, message)

        print(f"Email sent to {to} with subject '{subject}'")
    except Exception as e:
        print(f"Failed to send email: {e}")