# unobserveproperty test
# oneOf in dataSchema test
# maxItems in dataSchema
# null schema in oneOf

import paho.mqtt.client as mqtt
from random import uniform
import json

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("testOneOf")
    client.subscribe("testMaxItems")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
   
    
    if (msg.topic == "testOneOf"):
        rNumber = uniform(1, 10)
        print(rNumber)
        if (rNumber < 3):
            client.publish("oneOfTest","smaller than 3")
        elif (rNumber < 7):
            client.publish("oneOfTest", 6)
        else:
            client.publish("oneOfTest", json.dumps(None))
      
    if (msg.topic == "testMaxItems"):
        rNumber = uniform(1, 10)
        print(rNumber)
        if (rNumber < 3):
            client.publish("maxItemsTest", json.dumps((1, 2, 2)))
        elif (rNumber < 7):
            client.publish("maxItemsTest", json.dumps((1, 2)))
        else:
            client.publish("maxItemsTest", json.dumps((1, 1, 2, 2, 3)))
        


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
