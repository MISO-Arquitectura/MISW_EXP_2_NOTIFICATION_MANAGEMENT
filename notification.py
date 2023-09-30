from celery import Celery
from celery.signals import task_postrun
import smtplib 
from email.message import EmailMessage

celery_app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@celery_app.task(name='log.registrar')
def enviar_log(datos_log):

    email_subject = "Intruso detectado" 
    sender_email_address = "testcouponsmeli@gmail.com" 
    receiver_email_address = "ricardito9411@gmail.com" 
    email_smtp = "smtp.gmail.com" 
    email_password = "cguh pbsz ratk fnfu" 

    # Create an email message object 
    message = EmailMessage() 
    # Configure email headers 
    message['Subject'] = email_subject 
    message['From'] = sender_email_address 
    message['To'] = receiver_email_address 
    # Set email body text 
    message.set_content(f'Se ha detectado una solicitud inusual desde la ip: {datos_log["request"]["ip_address"]}') 
    # Set smtp server and port 
    server = smtplib.SMTP(email_smtp, '587') 
    # Identify this client to the SMTP server 
    server.ehlo() 
    # Secure the SMTP connection 
    server.starttls() 
    # Login to email account 
    server.login(sender_email_address, email_password) 
    # Send email 
    server.send_message(message) 
    # Close connection to server 
    server.quit()


    