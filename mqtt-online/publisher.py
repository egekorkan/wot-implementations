# unobserveproperty test
# oneOf in dataSchema test
# maxItems in dataSchema
# null schema in oneOf

# DONE: TODO: td-context-default-language , so putting @language in @context
# DONE: TODO: td-data-schema_contentMediaType and encoding
# DONE: TODO: exclusiveMinMax
# DONE: TODO: multipleOf
# DONE: TODO: pattern
# DONE: TODO: const
# DONE: TODO: anchor link
# DONE: TODO: contentCoding inside forms -> might be difficult
# DONE: TODO: default
# DONE: TODO: td-vocab-hreflang--Link
# DONE: TODO: see about cancel and query actions
# DONE: TODO: see about auto security
# DONE: TODO: sizes in links

import paho.mqtt.client as mqtt
from random import uniform
import json
import gzip
import time
import threading
import os

elapsed = 0

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("EgeMyPublisher/testOneOf")
    client.subscribe("EgeMyPublisher/testMaxItems")
    client.subscribe("EgeMyPublisher/testEncoding")
    client.subscribe("EgeMyPublisher/testFormEncoding")
    client.subscribe("EgeMyPublisher/testAction")
    client.subscribe("EgeMyPublisher/testAction/cancel")
    f = open("publisher.json", "r")
    client.publish("EgeMyPublisher/egeTestTD",f.read(),retain=True)

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
   
    
    if (msg.topic == "EgeMyPublisher/testOneOf"):
        rNumber = uniform(1, 10)
        # print(rNumber)
        if (rNumber < 2):
            client.publish("EgeMyPublisher/oneOfTest","smaller than 3")
        elif (rNumber < 4):
            client.publish("EgeMyPublisher/oneOfTest", 6*int(rNumber))
        elif (rNumber < 5):
            client.publish("EgeMyPublisher/oneOfTest", 6*rNumber)
        elif (rNumber < 6):
            client.publish("EgeMyPublisher/oneOfTest", "(888)555-1212")
        elif (rNumber < 8):
            client.publish("EgeMyPublisher/oneOfTest", "555-1212")
        else:
            client.publish("EgeMyPublisher/oneOfTest", json.dumps(None))
      
    if (msg.topic == "EgeMyPublisher/testMaxItems"):
        rNumber = uniform(1, 10)
        # print(rNumber)
        if (rNumber < 3):
            client.publish("EgeMyPublisher/maxItemsTest", json.dumps((1, 2, 2)))
        elif (rNumber < 7):
            client.publish("EgeMyPublisher/maxItemsTest", json.dumps((1, 2)))
        else:
            client.publish("EgeMyPublisher/maxItemsTest", json.dumps((1, 1, 2, 2, 3)))
    if (msg.topic == "EgeMyPublisher/testEncoding"):
        client.publish("encodingTest", json.dumps("iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII="))
    if (msg.topic == "EgeMyPublisher/testFormEncoding"):
        with gzip.open('seattle-weather-hourly-normals.csv.gz', 'rb') as f:
            file_content = f.read()
            client.publish("EgeMyPublisher/formEncodingTest",file_content,retain=True)
    if (msg.topic == "EgeMyPublisher/testAction"): #FIXME: This actually does not work, it blocks the loop
        global elapsed
        toElapse = int(msg.payload)
        # info = client.publish("EgeMyPublisher/actionTest/remaining", json.dumps(toElapse-elapsed))
        # print(info.mid)
        while elapsed < toElapse:
            
            print(toElapse-elapsed)
            client.publish("EgeMyPublisher/actionTest/remaining", json.dumps(toElapse-elapsed))
            client.loop_stop()
            time.sleep(1)
            elapsed = elapsed+1
            client.loop_start()
            
        elapsed = 0
        if toElapse > 5:
            client.publish("EgeMyPublisher/actionTest", json.dumps("that took a while"))
        else:
            client.publish("EgeMyPublisher/actionTest", json.dumps("that was quick"))
    if (msg.topic == "EgeMyPublisher/testAction/cancel"):
        elapsed = 10
        client.publish("EgeMyPublisher/actionTest", json.dumps("action canceled :-("))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

time.sleep(20)

client.disconnect()
client.loop_stop()
