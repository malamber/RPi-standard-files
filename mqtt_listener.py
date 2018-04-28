import paho.mqtt.client as mqtt

MQTT_SERVER = "130.205.36.11"
MQTT_3D = "/devices/3d/#"
MQTT_ALL = "/all/#"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if (msg.topic.find("/all") > 0) :
        print(msg.topic+" "+str(msg.payload))
    else if (msg.topic.find("/all") > 0):
        print(msg.topic+" "+str(msg.payload))
        #
    # more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
