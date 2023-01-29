
import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver

def sendMail(email_receiver,temp,hum,presence ):
    email_sender = 'alert.poulailler51@gmail.com'
    email_password = 'kvammvtyzerngqnt'
    email_receiver = 'aksel.paulet@gmail.com'
                    
    subject = 'ALERT POULAILLER CNRS'
    body = f"""Bonjour,
                                
Ce message survient a une alerte dans votre poulailler.
                                       
    Ci-dessous les relever pouvant être a l'origine : 
                                                    
        Température : {temp} °c
        Humidité : {hum} %
        {"PRESENCE DANS L'ENCLO" if presence else "aucune présence détectée"}
"""
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
