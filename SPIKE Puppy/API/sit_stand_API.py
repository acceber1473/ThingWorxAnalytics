# July 22nd- making code more efficient!!

# collecting data and uploading takes 4 minutes 
# creating dataset and waiting until complete takes 1.5 minutes 
# training model takes 3 minutes 
# predicting and executing takes 9-10 seconds 
# total of an almost 9 minute process
# download code on spike 

import hub, utime
import utime, os, ujson
import passwords as p
from Backpack_Code import Backpack


commands = '''
\x05
# Importing 
import ESPClient, ujson

# Initializing 
ESPClient.wifi('SSID','PASS')

PORT = 443

base='pp-21060114127e.portal.ptc.io'

# for properties
request='%s /Thingworx/Things/%s/Properties/%s HTTP/1.1\\r\\n'
request += 'Host: %s\\r\\n' % base
request += 'Content-Type: application/json\\r\\n'
request += 'Accept: application/json\\r\\n'
request += 'appKey: KEY \\r\\n'


# for services 
requestSer='%s /Thingworx/Things/%s/Services/%s HTTP/1.1\\r\\n'
requestSer += 'Host: %s\\r\\n' % base
requestSer += 'Content-Type: application/json\\r\\n'
requestSer += 'Accept: application/json\\r\\n'
requestSer += 'appKey: KEY \\r\\n'


def readIt(thing, property):
    req = request % ('GET',thing,property)
    req += '\\r\\n'
    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            Json = reply.split("\\r\\n")[-3]
            response = ujson.loads(Json)['rows'][0]
            return code, response[property]
        else:
            return code, reason
    except:
        return (-1, reply)


def writeIt(thing, property, value):
    payload = {property: value}
    payload = ujson.dumps(payload)
    req = request % ('PUT',thing,"*")
    req += 'Content-Length: %d\\r\\n\\r\\n' % len(payload)
    req += '%s\\r\\n\\r\\n' % payload

    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            return code, reply
        else:
            return code, reason
    except:
        return (-1, reply)

def writeIt2(thing, property1, value1, property2, value2):
    payload = {property1: value1, property2:value2}
    payload = ujson.dumps(payload)
    req = request % ('PUT',thing,"*")
    req += 'Content-Length: %d\\r\\n\\r\\n' % len(payload)
    req += '%s\\r\\n\\r\\\\n' % payload

    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            return code, reply
        else:
            return code, reason
    except:
        return (-1, reply)


def serviceRun(Thing, Service):
     req = requestSer % ('POST', Thing, Service)
     req += '\\r\\n'
     code, reason, reply = ESPClient.REST(base, PORT, req, True, timeout = 30.0)
     try:
          if code == 200:
               return code, reply
          else:
               return code, reason
     except:
          return(-1, reply)


def checkDatasetStatus():
     req = requestSer % ('POST', "PuppyThing", "checkDatasetStatus")
     req += '\\r\\n'
     code, reason, reply = ESPClient.REST(base, PORT, req, False)
     
     reply = reply[4:-3]
     
     #print(reply)
     reply = ujson.loads(reply)
     reply = reply['rows'][0]['state']
     try:
          if code == 200:
               return code, reply
          else:
               return code, reason
     except:
          return(-1, reply)


def checkModelStatus():
     req = requestSer % ('POST', "PuppyThing", "checkModelStatus")
     req += '\\r\\n'
     code, reason, reply = ESPClient.REST(base, PORT, req, False)
     
     reply = reply[4:-3]
     
     #print(reply)
     reply = ujson.loads(reply)
     reply = reply['rows'][0]['state']
     try:
          if code == 200:
               return code, reply
          else:
               return code, reason
     except:
          return(-1, reply)  

def prediction():
     req = requestSer % ('POST', "PuppyThing", "predictScoring")
     req += '\\r\\n'
     code, reason, reply = ESPClient.REST(base, PORT, req, False, timeout = 10.0)
     
     reply = reply[4:-3]
     
     reply = ujson.loads(reply)
     reply = reply['rows'][0]['state']
     try:
          if code == 200:
               return code, reply
          else:
               return code, reason
     except:
          return(-1, reply)

def getPrediction():
    an = prediction()
    answer = an[1]
    if answer.count('stand')==2:
        result = 'stand'
    elif answer.count('sit')==2:
        result = 'sit'
    else:
        result = 'whoops'
    return result


\x04
'''

commands = commands.replace('SSID',p.SSID)
commands = commands.replace('PASS',p.KEY)
commands = commands.replace('KEY',p.appKeys['Thingworx'])

dongle = Backpack(hub.port.C, verbose = True) 
# if verbose is true you can switch to the backpack mode 

def configure():
    if not dongle.setup(): return False
    for cmd in commands.split('\n'):
        if not dongle.EOL(dongle.ask(cmd)) : return False
    return True

def grab(Thing, Property):
    dongle.ask()
    reply = dongle.ask('readIt("%s","%s")' % (Thing, Property))
    try:
        return reply.split('\r\n')[-2]
    except: 
        return None
        
        
def set(Thing, Property, Value):
    dongle.ask()
    reply = dongle.ask('writeIt("%s","%s","%s")' % (Thing, Property, Value))
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None
def set2(Thing, Property1, Value1, Property2, Value2):
    dongle.ask()
    reply = dongle.ask('writeIt2("%s","%s","%s","%s","%s")' % (Thing, Property1, Value1, Property2, Value2))
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None

def callService(Thing, Service):
    dongle.ask()
    reply = dongle.ask('serviceRun("%s","%s")' % (Thing, Service))
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None


def dataSetStatus():
    dongle.ask()
    reply = dongle.ask('checkDatasetStatus()[1]')
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None

def modelStatus():
    dongle.ask()
    reply = dongle.ask('checkModelStatus()[1]')
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None 

def getPrediction():
    dongle.ask()
    reply = dongle.ask('getPrediction()')
    dongle.ask()
    try:
        return reply.split('\r\n')[1] # change to 5 sometimes
    except: 
        return None 


configure()   

##########################################
# intialize puppy 
dist_sensor = hub.port.B.device  
legR = hub.port.A.motor                                                                                    
legL = hub.port.E.motor   
button = hub.port.F.device                                                                                 
legR.mode(2)                                                                                               
legL.mode(2)

begR = legR.get()[0]
begL = legL.get()[0]

sitR = begR-60
sitL = begL-60

trainingSit = []
trainingStand = []
sitArray = []
standArray = []
stateArray = []
distanceArray = []

def sit():
    print('sitting')
    legR.run_to_position(sitR, 30)
    legL.run_to_position(sitL,30)

def stand():
    print('standing')
    legR.run_to_position(begR,50)
    legL.run_to_position(begL,50)

######################################
print('calling refresh service')
        
callService('PuppyThing2', 'refresh')
utime.sleep(0.1)    
######################################

###############################################################
while True:  
    utime.sleep(0.2)
    if hub.button.left.is_pressed():
        # Record a command A observation- sit
        dist = dist_sensor.get()[0]
        dog_command = 'A'
        print('Puppy learns that this means command A (sit)')
        utime.sleep(0.2)
        if dist != None:  # Parses out the null values 
            # Adds the observation to the recorded data
            trainingSit.append(dist)
            print(dist,dog_command)
        
    elif hub.button.right.is_pressed():
        # Record a command B observation- stand
        dist = dist_sensor.get()[0]
        dog_command = 'B'
        print('Puppy learns that this means command B (stand)')
        utime.sleep(0.2)
        if dist != None:
            # Adds the observation to the recorded data
            trainingStand.append(dist)
            print(dist,dog_command)
        
    elif hub.button.center.is_pressed():
        # Stop training
        dist = 0
        dog_command = 'Exit'
        print('Puppy is done training for now.')
        print(dist, dog_command)
        break
    else:
        continue


print(trainingSit)
print(trainingStand)

hub.sound.beep()

#####################################################

for i in range(0,len(trainingSit)):
    stateArray.append("sit")
    distanceArray.append(trainingSit[i])
for j in range(0,len(trainingStand)):
    stateArray.append("stand")
    distanceArray.append(trainingStand[j])
for k in range (0, len(distanceArray)):
  set2("PuppyThing", "distance", distanceArray[k], "state", stateArray[k]) 

print('uploaded data')
hub.sound.beep()

#####################################################

print('creating data set now ....')
callService('PuppyThing', 'createDataset2')

hub.sound.beep()

#####################################################

print('about to try and train a model lmao ')
while True:
  utime.sleep(1)
  if dataSetStatus() == "'COMPLETED'":
    break
  else:
    continue

#hub.sound.beep()

callService('PuppyThing', 'trainModel')
while True:
  utime.sleep(5)
  if modelStatus() == "'COMPLETED'":
    break
  else:
    continue
    
hub.sound.beep()

print('finished building the model!')

while True:  
    utime.sleep(0.1)
    buttonPress = button.get()[0]
    if buttonPress > 8:
        hub.sound.beep()
        dist = dist_sensor.get()[0]
  
        if dist != None:  
            set('PuppyThing', 'distance', dist)
            result = getPrediction()
            if result.count('stand'):
                stand()
            elif result.count('sit'):
                sit()               
    else:
        continue


#while True:  
#    utime.sleep(0.2)
#    if hub.button.left.is_pressed():
#        hub.sound.beep()
#        dist = dist_sensor.get()[0]
  
#        if dist != None:  
#            set('PuppyThing', 'distance', dist)
#            result = getPrediction()
#            if result.count('stand'):
#                stand()
#            elif result.count('sit'):
#                sit()               
#    else:
#        continue



#while True:
#    dist = dist_sensor.get()[0]
#    if dist!= None:
#        currentState = getPrediction()
#        if currentState != previousState:
#            set('PuppyThing', 'distance', dist)
#            previousState= getPrediction()
#            if result.count('stand'):
#                stand()
#            elif result.count('sit'):
#                sit()
#            previousState = currentState
#        else:
#            previousState = previousState
#    else:
        
#        continue 

        
        
