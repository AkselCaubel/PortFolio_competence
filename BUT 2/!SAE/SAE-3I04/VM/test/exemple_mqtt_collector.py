import paho.mqtt.client as mqtt
from random import choice
from time import sleep

import influx


def getRandId(): # ID Generator with a lengh of 16 | OUTPUT Str
    char = "azertyuiopqsdfghjklmwxcvbn0123456789AZERTYUIOPQSDFGHJKLMWXCVBN"
        
    return "".join(str(choice(char) for i in range (16)))


def jumpLine(x:int): # Break {x} ligne in the shell | INTPUT Int
    for i in range(x):
        print()

def on_message(client, userdata, message): # when a topic arrive, it's send to influx | INPUT It's automaticly
    influx.dataPush(message.topic.split('/')[1],message.topic.split('/')[2],str(message.payload.decode("utf-8")))

def on_info(client, userdata, message):
    influx.infoPush(message.topic,str(message.payload.decode("utf-8")))


brokerIp = "*.*.*.*" # Need to be a String
brokerPort = 456  # Need to be a Int
dataType = ["co2","hum","tem"] # All dataType to listen

listener = {} # Init a dict var  for the litener

for type in dataType: 

    # Init of all listener whith them topic

    topic = f"data/+/{type}"
    
    listener[type] = mqtt.Client(getRandId())
    listener[type].username_pw_set('admin', password='***') # Set se login to the MQTT-Broker
    listener[type].connect(brokerIp,brokerPort,60)
    listener[type]._send_connect = print(f"listener {type} : trying to connect...") # SIN
    listener[type].on_connect = print(f"listener {type} : Connected on {brokerIp}:{brokerPort}") # SIN ACK
    listener[type].on_message = on_message # exec on_message when a message arrive
    listener[type].subscribe(topic) # listen on the topic
    listener[type].loop_start() # listen begin | Use a thread

jumpLine(2)

topic =f"esp/+/info/#"

listener["info"] = mqtt.Client(getRandId())
listener["info"].username_pw_set('****', password='****') # Set se login to the MQTT-Broker
listener["info"].connect(brokerIp,brokerPort,60)
listener["info"]._send_connect = print(f"listener info : trying to connect...") # SIN
listener["info"].on_connect = print(f"listener info : Connected on {brokerIp}:{brokerPort}") # SIN ACK
listener["info"].on_message = on_info # exec on_info when a message arrive
listener["info"].subscribe(topic) # listen on the topic
listener["info"].loop_start() # listen begin | Use a thread


jumpLine(2)
print("All listener are ok") 
jumpLine(2)
while True: # Infinit loop for listen always
    sleep(600)