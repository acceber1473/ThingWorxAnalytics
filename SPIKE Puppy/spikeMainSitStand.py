import hub, utime, ujson
from Backpack_Code import Backpack

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
    utime.sleep(5)

def stand():
    print('standing')
    legR.run_to_position(begR,50)
    legL.run_to_position(begL,50)
    utime.sleep(5)


# Setup Dongle
dongle = Backpack(hub.port.C, verbose = False) 

def main():
    global a
    a = ' '
    # This Messages can be defined in a function on the Spike
    # dongle.ask() sends the message to ESP uart. In this setup the ESP's REPL has been turned off  
    response = dongle.ask(msgStr)
    if response.count('sit'):
        sit()
    elif response.count('stand'):
        stand()
    elif response.count('modelCompleted'):
        a = 'complete'

    
# dongle.ask() is blocking and waits for ">>>"

    response = response.replace('>','')
    
    print("response:", response)
    if response == '' or response == ">>>":
        response = dongle.read()

#msg = {'example Key': 'example value'}
#msgStr = 'refresh'
#main()
utime.sleep(0.5)
while True:  
    utime.sleep(0.2)
    msg = {}
    if hub.button.left.is_pressed():
        # Record a command A observation- sit
        dist = dist_sensor.get()[0]
        utime.sleep(0.5)
        print('Puppy learns that this means command A (sit)')
        
        if dist != None:  # Parses out the null values 
            # Adds the observation to the recorded data
            msg['distance'] = dist
            state = 'sit'
            msg['state'] = state
            msgStr = ujson.dumps(msg)
            main()
            print(dist, 'sit')
        
    elif hub.button.right.is_pressed():
        # Record a command B observation- stand
        dist = dist_sensor.get()[0]
        utime.sleep(0.5)
        print('Puppy learns that this means command B (stand)')
        
        if dist != None:
            # Adds the observation to the recorded data
            msg['distance'] = dist
            state = 'stand'
            msg['state'] = state
            msgStr = ujson.dumps(msg)
            main()
            print(dist, 'stand')
        
    elif hub.button.center.is_pressed():
        # Stop training
        print('Puppy is done training for now.')
        break
    else:
        continue
utime.sleep(1)        
msgStr = 'csv'
main()
utime.sleep(20)
msgStr = 'hi'
while True:
    main()
    if a == 'complete':
        break
    #if stateModel == 'completed':
    #    break
    utime.sleep(2)
print('training done!')

utime.sleep(0.5)

#while True:
#    utime.sleep(0.2)
#    msg = {}
#    if button.get()[0] > 8:
#        dist = dist_sensor.get()[0]
#        print(dist)
       
#        if dist != None:
#            msg['distance'] = dist
#            msg['predictState'] = 'predict'
#            msgStr = ujson.dumps(msg)
#            main()
while True:
    utime.sleep(0.5)
    msg = {}
    
    dist = dist_sensor.get()[0]
    print(dist)
   
    if dist != None:
        msg['distance'] = dist
        msg['predictState'] = 'predict'
        msgStr = ujson.dumps(msg)
        main()
    print('predicted!')
        
        


while True:
    msg = ''
    main()
    utime.sleep(1)


#while True:
#    main()
#    utime.sleep(0.5)


    
