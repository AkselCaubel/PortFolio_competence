import paho.mqtt.client as mqtt
from time import sleep
from rich import print as pprint
import json
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import base64

ttnToken_iot51:str="NNSXS.3BVJF3YWR6MKUSJUGRYSI4K665V3TVYZZD6CK7Y.PTPMIRWO4ORECVZLDRJOIOAU4EXQ4JTVC3QYTDZ7CUBH6YK6BR3Q"
ttnToken_projetiot:str="NNSXS.E6CNY5PDHM4MZXGFCFFTAQV6ZMIVHBNRJM7KSJI.5V2VVNHW6MUAZNTCSO27WBLHE34Y6IVRLIGGTZF4WZG4TDHDQEDQ"
ttnToken_kirikou:str="NNSXS.3BVJF3YWR6MKUSJUGRYSI4K665V3TVYZZD6CK7Y.PTPMIRWO4ORECVZLDRJOIOAU4EXQ4JTVC3QYTDZ7CUBH6YK6BR3Q"
ttnToken_lr:str = "NNSXS.CRRMZSLD77FVBPH56YD6US7UGW3J7HSXPAZORRY.WOJ3P3VJCADEW3MQO64FEBABOLBIHDMIWFOELWN5P4GVBT5V2HIA"

ttnLogin:list[tuple,...] = [ # (UserId,ttnToken)
    ("iutbiot51@ttn","NNSXS.3BVJF3YWR6MKUSJUGRYSI4K665V3TVYZZD6CK7Y.PTPMIRWO4ORECVZLDRJOIOAU4EXQ4JTVC3QYTDZ7CUBH6YK6BR3Q"),
    ("iotapplication@ttn","NNSXS.E6CNY5PDHM4MZXGFCFFTAQV6ZMIVHBNRJM7KSJI.5V2VVNHW6MUAZNTCSO27WBLHE34Y6IVRLIGGTZF4WZG4TDHDQEDQ"),
    ("sae304-test-sensors@ttn","NNSXS.CRRMZSLD77FVBPH56YD6US7UGW3J7HSXPAZORRY.WOJ3P3VJCADEW3MQO64FEBABOLBIHDMIWFOELWN5P4GVBT5V2HIA")
    ]


def on_message(client, userdata, message):

            
    jsonData = json.loads(message.payload.decode('utf-8'))
    
    
    bucket = "IUT_Devices"
    token = "NZuKx9nuCgkreX6PJ7jd2IdEGNVAosqmxcJUnJi944WTODCL-XJ1WXcAEHcMwmpEbML20G4P60QEr99YiU-xcg=="
    
    client = InfluxDBClient(url="http://51.158.110.29:8086", token=token, org="iutbeziers") # Login to Influx
    write_api = client.write_api(write_options=SYNCHRONOUS) # Write mode + synchronise
    
    device = jsonData["end_device_ids"]["dev_eui"]
    
    if device == "A81758FFFE086F8D" or device == "A81758FFFE086F90" or device == "A81758FFFE086F91" : # Capteur de mouvement poulailler 1 | 1 | 2
        
        hum,light,motion,temperature,vdd = jsonData.get('uplink_message').get('decoded_payload').values()
        
        # Init des différents relever
        h = Point("sensors").tag("device",device).field("hum",float(hum))
        l = Point("sensors").tag("device",device).field("lux",light)
        m = Point("sensors").tag("device",device).field("motion",motion)
        t = Point("sensors").tag("device",device).field("temp",float(temperature))
        v = Point("sensors").tag("device",device).field("vdd",vdd/1000)
        
        # Ecriture des différents relever dans InfluxDB
        write_api.write(bucket=bucket, record=h)
        write_api.write(bucket=bucket, record=l)
        write_api.write(bucket=bucket, record=m)
        write_api.write(bucket=bucket, record=t)
        write_api.write(bucket=bucket, record=v)
    
        print(f"{device} print data")
    
    elif device == "70B3D5E820002D69" :
        rawPayload = jsonData.get('uplink_message').get('frm_payload')
        hexPayload = base64.b64decode(rawPayload).hex()
        
        if hexPayload.startswith("4e"):
            test = "4e606c5ff5070430bdaa204e80606c600a070430bdaa204e80"
            lenId = test[10:12]
            ID = test[12:12+(int(lenId))*2]
            print(lenId)
            
            num_of_bits = int(lenId)*8

            binData = bin(int(ID, 16))[2:].zfill(num_of_bits)
            ID = int(binData,2)
            
            i = Point("sensors").tag("device",device).field("id",ID)
            write_api.write(bucket=bucket, record=i)
            
    
    client.close() # Close the Influx connexion
    



brokerIp = "eu1.cloud.thethings.network" # Need to be a String
brokerPort = 1883  # Need to be a Int

listener:dict = {}

for userId, ttnToken in ttnLogin:
    topic = f"v3/{userId}/devices/+/up"


    listener[userId] = mqtt.Client()
    listener[userId].username_pw_set(userId, password=ttnToken) # Set se login to the MQTT-Broker
    listener[userId].connect(brokerIp,brokerPort,60)
    listener[userId]._send_connect = print(f"listener {userId} : trying to connect...") # SIN
    listener[userId].on_connect = print(f"listener {userId} : Connected on {brokerIp}:{brokerPort}") # SIN ACK
    listener[userId].on_message = on_message # exec on_message when a message arrive
    listener[userId].subscribe(topic) # listen on the topic
    listener[userId].loop_start() # listen begin | Use a thread
    print("\n\n")

print("All listenner are ok !")

print("\n")

while True:
    sleep(5000)
