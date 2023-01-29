import requests
import json
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep



while True:
    login = "6334446bbdcbd20e4daf92b4"
    password = "3806e9d6cead4f45803df27eee00994a"
    authentication = (login, password)

    device = "B44949"

    response = requests.get(f"https://backend.sigfox.com/api/v2/devices/{device}/messages",
    auth=authentication)

    jsonData = json.loads(response.text)
    lastData = jsonData["data"][0]


    my_hexdata = lastData['data']


    scale = 16 ## equals to hexadecimal

    num_of_bits = len(my_hexdata)*4

    binData = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    print("Rbatterie",int(binData[:5],2))
    batterie = (int(binData[:5],2)* 0.05) + 2.7

    reserved = binData[5:8]
    dataType = binData[8:13]
    print(dataType)

    flag = binData[13:14]
    print(binData[14:24])
    dataTmp = (int(binData[14:24],2)-200)/8

    dataHum = int(binData[24:32],2)/2
    print(binData[24:32])

    bucket = "IUT_Devices"
    token = "NZuKx9nuCgkreX6PJ7jd2IdEGNVAosqmxcJUnJi944WTODCL-XJ1WXcAEHcMwmpEbML20G4P60QEr99YiU-xcg=="


    client = InfluxDBClient(url="http://51.158.110.29:8086", token=token, org="iutbeziers") # Login to Influx
    write_api = client.write_api(write_options=SYNCHRONOUS) # Write mode + synchronise

    t = Point("sensors").tag("device",device).field("temp",dataTmp) # create the influx point
    h = Point("sensors").tag("device",device).field("hum",dataHum) # create the influx point

    #write_api.write(bucket=bucket, record=t) # write
    #write_api.write(bucket=bucket, record=h) # write

    print(f"Data push : tmp = {dataTmp} | hum = {dataHum}")
    client.close()

    print(dataTmp)
    print(dataHum)

    sleep(60*10)
