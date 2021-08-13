import random
import ujson as json

sub_topics = []
pub_topics = []

client = None

def sub_cb(topic, msg):
    '''
    The callback function that is called whenever client.check_msg() or client.wait_msg() finds a message to a topic the ESP is subscribed to
    '''
    if topic == MQTT_CONFIG["SUB_TOPIC1"] :
        msgStr = msg.decode('utf-8')
        spike_write(msgStr)
    elif topic == MQTT_CONFIG["SUB_TOPIC2"] : 
        pass
    # Add another if statement for each topic you are subscribed to
        
def connect_and_subscribe():
    '''
    Helper function to connect this client to a MQTT Broker and Subscribe to the topics specified in the MQTT CONFIG file
    '''
    global client
    client = MQTTClient(client_id = MQTT_CONFIG["CLIENT_ID"], server = MQTT_CONFIG["MQTT_BROKER"], port = MQTT_CONFIG["PORT"])
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to %s MQTT broker' % (MQTT_CONFIG["MQTT_BROKER"]), end=" ")
    subscribe(client)
    setup_publish(client)
    return client
    
def subscribe(client):
    '''
    Subscribes to all of the non-empty topics in the MQTT Config File 
    '''
    for key in MQTT_CONFIG:
        if key.startswith("SUB") and str(type(MQTT_CONFIG[key])) == "<class 'bytes'>" and MQTT_CONFIG[key] != b'':
            client.subscribe(MQTT_CONFIG[key])
            print('subscribed to %s topic' % (MQTT_CONFIG[key]), end = ", ")
            sub_topics.append(MQTT_CONFIG[key])
    print()
    
def restart_and_reconnect():
    '''
    If the client fails to connect to the MQTT Broker, restart the chip
    '''
    print('Failed to connect to MQTT broker. Reconnecting...')
    utime.sleep(10)
    machine.reset()
    
def spike_waitMSG():
    '''
    Wait for a server message.The message will be delivered to spike_callBack().
    (Blocking Function) (REPL MUST BE OFF)
    '''
    response = None

    while (response == None or response == b''):
        response = uart.readline()
    spike_write(">>>") # Immediately send to EOL statement to return from dongle.ask()
    return response
    
def spike_checkMSG():
    '''
    Check if there is a pending message from server. If yes, process the same way as spike_waitMSG(), if not, return immediately. (REPL MUST BE OFF)
    '''
    response = uart.readline()
    if response != b'':
        spike_write(">>>") # Immediately send to EOL statement to return from dongle.ask()
        return response
    else :
        return None
        
def spike_write(msg):
    '''
    Send a message to the Spike Prime over uart communication (REPL can be on or off)
    '''
    uart.write(msg)
    
def setup_publish(client):
    '''
    Create an array of all of the publish topics and publishes a simple message to all of them
    '''
    for key in MQTT_CONFIG:
        if key.startswith("PUB") and str(type(MQTT_CONFIG[key])) == "<class 'bytes'>" and MQTT_CONFIG[key] != b'':
            pub_topics.append(MQTT_CONFIG[key])
    publish_all("Connected to %s" % MQTT_CONFIG['CLIENT_ID'])

def publish_all(msg):
    '''
    Sends a message to every topic this client wants to publish to
    '''
    global client
    for topic in pub_topics:
        client.publish(topic, msg)

def main():
    '''
    Example of a main.py
    '''
    try:
        client = connect_and_subscribe()
    except OSError as e:
        restart_and_reconnect()
    uos.dupterm(None, 1) # Turn the REPL off to be able to read a message into a variable
    while True:
        spikeMsg = spike_waitMSG()
        if (spikeMsg == b'\x03\r\n' or spikeMsg == b'\x03'):
           # Turn the REPL back on if a Ctrl+C is received
           uos.dupterm(uart, 1)
           print("Got a Ctrl+C")
           break
        if spikeMsg != b'':
            client.publish(MQTT_CONFIG["PUB_TOPIC1"], spikeMsg)
        
        client.check_msg()
        utime.sleep(0.1)
    client.disconnect()
    
main()
