#coding: utf-8

# Hayakawa Laboratory's presence status display application.
# Use 'getBeebotteCert.sh' and prepare the Beebotte certificate in the same directory.
#
# Created by aoisupersix.

import os
import paho.mqtt.client as mqtt

env = {}
# API_TOKEN = env["BEEBOTTE_HLAB_API_TOKEN"]
HOSTNAME = "mqtt.beebotte.com"
PORT = 8883
TOPIC = "hlab/in"
CACERT = "mqtt.beebotte.com.pem"

def init():
    #環境変数の読み込み
    envFile = open(".env", "r")
    lines = envFile.readlines()
    for line in lines:
        line = line.strip()
        name = line.split("=")[0]
        val = line.split("=")[1]
        env.update({name: val})

def on_connect(client, userdata, dc, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC, 1)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

init()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("token:" + env["BEEBOTTE_HLAB_API_TOKEN"])
client.tls_set(CACERT)
client.connect(HOSTNAME, PORT, 60)
client.loop_forever()
