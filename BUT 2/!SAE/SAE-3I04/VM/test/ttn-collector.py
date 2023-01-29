import paho.mqtt.client as mqtt
from time import sleep

ttnToken:str="NNSXS.3BVJF3YWR6MKUSJUGRYSI4K665V3TVYZZD6CK7Y.PTPMIRWO4ORECVZLDRJOIOAU4EXQ4JTVC3QYTDZ7CUBH6YK6BR3Q"

"""mosquitto_sub -h eu1.cloud.thethings.network -t "#" -u "iutbiot51@ttn" -P "NNSXS.3ETOT24RSAQ7RTFCJ6VENFLLTLHXYOWVNSKYRUQ.ZXFLTN2VXJGHD4UYHTDF676XZH3KFGQZSEHRES7XNS65ABSGOB6A" -d"""

def on_message(client, userdata, message):
    try:
        print(f"topic : {message.topic}\n")
        print(f"payload : {str(message.payload.decode('utf-8'))}\n\n")
    except TypeError:
        pass
    #influx.infoPush(message.topic,str(message.payload.decode("utf-8")))


brokerIp = "eu1.cloud.thethings.network" # Need to be a String
brokerPort = 1883  # Need to be a Int



#topic = "v3/iutbiot51@ttn/devices/+/up"
topic = "v3/sae304-test-sensors@ttn/devices/+/up"

listener = mqtt.Client()
listener.username_pw_set('iutbiot51@ttn', password=ttnToken) # Set se login to the MQTT-Broker
listener.connect(brokerIp,brokerPort,60)
listener._send_connect = print(f"listener ttn : trying to connect...") # SIN
listener.on_connect = print(f"listener ttn : Connected on {brokerIp}:{brokerPort}") # SIN ACK
listener.on_message = on_message # exec on_message when a message arrive
listener.subscribe(topic) # listen on the topic
listener.loop_start() # listen begin | Use a thread

while True:
    sleep(5000)