
import smtplib
import ssl
from email.message import EmailMessage
from influxdb_client import InfluxDBClient

# Define email sender and receiver

def sendMailAlert(temp,hum,presence): # sendMail(email_receiver,temp,hum,presence )
    email_sender = 'alerte.poulailler51@gmail.com'
    email_password = 'ptaoelxvsbrniany'#'kvammvtyzerngqnt'
    #email_receiver = 'arnaud.pruvost@etu.umontpellier.fr'
    email_receiver = 'aksel.paulet@gmail.com'
                    
    subject = 'ALERTE Poulailler CNRS'
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
    print("creating ssl context")
    context = ssl.create_default_context()
    # Log in and send the email
    print("try login send")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        print("try")
        smtp.login(email_sender, email_password)
        print("login")
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("send")
        

def sendMailOk(temp,hum,presence): # sendMail(email_receiver,temp,hum,presence )
    email_sender = 'alerte.poulailler51@gmail.com'
    email_password = 'kvammvtyzerngqnt'
    email_receiver = 'aksel.paulet@gmail.com'
                    
    subject = 'ALERT POULAILLER CNRS'
    body = f"""Bonjour,
                                
Les constantes du poulailler sont à nouveaux correcte !
                                       
    Ci-dessous les relever pouvant être a l'origine : 
                                                    
        Température : {temp} °c
        Humidité : {hum} %
        {"PRESENCE DANS L'ENCLO" if presence else "aucune présence détectée"}
        
Un mail vous sera envoyé lorsque les constantes reviendront a la normale
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





def get_humTemp(devEUI):

    client = InfluxDBClient(
        url="http://51.158.110.29:8086",
        token="VXDczS854yyBIi11-_bQKsuYSi4Pik6W-FR3Cnf3rzNRArHWjjhPSNO_2cx_7u_15W1WuXm_L8v-mn7lytGRKA==",
        org="iutbeziers"
    )

    query_api = client.query_api()
    
    query = f'from(bucket: "IUT_Devices")\
  |> range(start: -1d)\
  |> last()\
  |> filter(fn: (r) => r["device"] == "{devEUI}")'
  
    result = query_api.query(org="iutbeziers", query=query)
    client.close()
    value:list[int] = []
    
    for table in result:
        for element in table :
            value.append(round(element.get_value(),2))
    
    return value


tempOk = True
  
hum ,temp = get_humTemp("B448E4")

print(f"Hum = {hum} | temp = {temp}")

if tempOk == True :
    print("temOK True")
    if temp < 15 or temp > 21:
        print("TempOK going to False")
        tempOk = False
        print("mailAlertCall")
        sendMailAlert(temp,hum,False)
        print("mailAlertSend")
        
    
else: # tempOk = False
    
    if temp >= 15 and temp <= 21:
        
        tempOk = True 
        
        sendMailAlertOk(temp,hum,False)
        