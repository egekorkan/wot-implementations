# unobserveproperty test
# oneOf in dataSchema test
# maxItems in dataSchema
# null schema in oneOf

import paho.mqtt.client as mqtt
from random import uniform

# The callback for when the client receives a CONNACK response from the server.

myTemp = 10

def on_disconnect(client, userdata, rc):
    print("disconnected")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("testMe")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload)+str(msg.retain))
   
    
    if (msg.topic == "testMe"):
        # print("got something")
        client.publish("temperature", myTemp + uniform(0, 1), retain=True)


client = mqtt.Client(client_id="TUMQTT")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("0m2m.net", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
