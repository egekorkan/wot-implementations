# unobserveproperty test
# oneOf in dataSchema test
# maxItems in dataSchema
# null schema in oneOf

# DONE: TODO: td-context-default-language , so putting @language in @context
# TODO: td-data-schema_contentMediaType and encoding
# DONE: TODO: exclusiveMinMax
# DONE: TODO: multipleOf
# DONE: TODO: pattern
# DONE: TODO: const
# DONE: TODO: anchor link
# TODO: contentCoding inside forms -> might be difficult
# TODO: default
# DONE: TODO: td-vocab-hreflang--Link
# TODO: see about cancel and query actions
# DONE: TODO: see about auto security
# DONE TODO: sizes in links

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
    client.subscribe("testEncoding")
    f = open("publisher.json", "r")
    client.publish("egeTestTD",f.read(),retain=True)

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
   
    
    if (msg.topic == "testOneOf"):
        rNumber = uniform(1, 10)
        # print(rNumber)
        if (rNumber < 2):
            client.publish("oneOfTest","smaller than 3")
        elif (rNumber < 4):
            client.publish("oneOfTest", 6*int(rNumber))
        elif (rNumber < 5):
            client.publish("oneOfTest", 6*rNumber)
        elif (rNumber < 6):
            client.publish("oneOfTest", "(888)555-1212")
        elif (rNumber < 8):
            client.publish("oneOfTest", "555-1212")
        else:
            client.publish("oneOfTest", json.dumps(None))
      
    if (msg.topic == "testMaxItems"):
        rNumber = uniform(1, 10)
        # print(rNumber)
        if (rNumber < 3):
            client.publish("maxItemsTest", json.dumps((1, 2, 2)))
        elif (rNumber < 7):
            client.publish("maxItemsTest", json.dumps((1, 2)))
        else:
            client.publish("maxItemsTest", json.dumps((1, 1, 2, 2, 3)))
    if (msg.topic == "testEncoding"):
        client.publish("encodingTest", json.dumps("iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII="))
        


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
