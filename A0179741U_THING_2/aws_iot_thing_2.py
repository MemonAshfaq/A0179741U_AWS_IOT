from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import random, time

import json
import enum


class dataDescription(enum.Enum):
    id          = 0
    cycle       = 1
    os1         = 2
    os2         = 3
    os3         = 4
    sensor1     = 5
    sensor2     = 6
    sensor3     = 7
    sensor4     = 8
    sensor5     = 9
    sensor6     = 10
    sensor7     = 11
    sensor8     = 12
    sensor9     = 13
    sensor10    = 14
    sensor11    = 15
    sensor12    = 16
    sensor13    = 17
    sensor14    = 18
    sensor15    = 19
    sensor16    = 20
    sensor17    = 21
    sensor18    = 22
    sensor19    = 23
    sensor20    = 24
    sensor21    = 25
    lineLength  = 26
    time_stamp   = 27
    matric_num  = 28

data_dict = {
    'id'        : None,
    'cycle'     : None,
    'os1'       : None,
    'os2'       : None,
    'os3'       : None,
    'sensor1'   : None,
    'sensor2'   : None,
    'sensor3'   : None,
    'sensor4'   : None,
    'sensor5'   : None,
    'sensor6'   : None,
    'sensor7'   : None,
    'sensor8'   : None,
    'sensor9'   : None,
    'sensor10'  : None,
    'sensor11'  : None,
    'sensor12'  : None,
    'sensor13'  : None,
    'sensor14'  : None,
    'sensor15'  : None,
    'sensor16'  : None,
    'sensor17'  : None,
    'sensor18'  : None,
    'sensor19'  : None,
    'sensor20'  : None,
    'sensor21'  : None,
    'time_stamp' : None,
    'mtrcNum'   : None

}

#open a file as read-only
rdfile = open('train_FD002.txt')


# A random programmatic shadow client ID.
SHADOW_CLIENT = "EE5111_A0179741U_THING_2"

# The unique hostname that &IoT; generated for 
# this device.
# ThisHasToBeUpdated
HOST_NAME = "a12d228r28ffvb-ats.iot.us-east-2.amazonaws.com"

# The relative path to the correct root CA file for &IoT;, 
# which you have already saved onto this device.
# ThisHasToBeUpdated
ROOT_CA = "AmazonRootCA1.pem.txt"

# The relative path to your private key file that 
# &IoT; generated for this device, which you 
# have already saved onto this device.
# ThisHasToBeUpdated
PRIVATE_KEY = "84df1ee4b2-private.pem.key"

# The relative path to your certificate file that 
# &IoT; generated for this device, which you 
# have already saved onto this device.
# ThisHasToBeUpdated
CERT_FILE = "84df1ee4b2-certificate.pem.crt"

# A programmatic shadow handler name prefix.
# ThisHasToBeUpdated
SHADOW_HANDLER = "EE5111_A0179741U_THING_1"

# Automatically called whenever the shadow is updated.
def myShadowUpdateCallback(payload, responseStatus, token):
  print()
  print('UPDATE: $aws/things/' + SHADOW_HANDLER + 
    '/shadow/update/#')
  print("payload = " + payload)
  print("responseStatus = " + responseStatus)
  print("token = " + token)

# Create, configure, and connect a shadow client.
myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,
  CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()

# Create a programmatic representation of the shadow.
myDeviceShadow = myShadowClient.createShadowHandlerWithName(
  SHADOW_HANDLER, True)

# Keep generating random test data until this script 
# stops running.
# To stop running this script, press Ctrl+C.

line = rdfile.readline()
while line:
    print(line)
    line = line.split()
    
    #override id value as FD001_<id>
    data_dict['id'] = 'FD002_' + line[dataDescription.id.value]
    
    #add time_stamp
    data_dict['time_stamp'] = time.time()
    
    #add matric number
    data_dict['mtrcNum'] = 'A0179741U'
    
    #read rest of the entries from line and add them to dict
    if len(line) != dataDescription.lineLength.value:
        print('ERROR: This line does not have enough data.')
        exit()
    
    data_dict['cycle']      = line[dataDescription.cycle.value]
    data_dict['os1']        = line[dataDescription.os1.value]
    data_dict['os2']        = line[dataDescription.os2.value]
    data_dict['os3']        = line[dataDescription.os3.value]
    data_dict['sensor1']    = line[dataDescription.sensor1.value]
    data_dict['sensor2']    = line[dataDescription.sensor2.value]
    data_dict['sensor3']    = line[dataDescription.sensor3.value]
    data_dict['sensor4']    = line[dataDescription.sensor4.value]
    data_dict['sensor5']    = line[dataDescription.sensor5.value]
    data_dict['sensor6']    = line[dataDescription.sensor6.value]
    data_dict['sensor7']    = line[dataDescription.sensor7.value]
    data_dict['sensor8']    = line[dataDescription.sensor8.value]
    data_dict['sensor9']    = line[dataDescription.sensor9.value]
    data_dict['sensor10']   = line[dataDescription.sensor10.value]
    data_dict['sensor11']   = line[dataDescription.sensor11.value]
    data_dict['sensor12']   = line[dataDescription.sensor12.value]
    data_dict['sensor13']   = line[dataDescription.sensor13.value]
    data_dict['sensor14']   = line[dataDescription.sensor14.value]
    data_dict['sensor15']   = line[dataDescription.sensor15.value]
    data_dict['sensor16']   = line[dataDescription.sensor16.value]
    data_dict['sensor17']   = line[dataDescription.sensor17.value]
    data_dict['sensor18']   = line[dataDescription.sensor18.value]
    data_dict['sensor19']   = line[dataDescription.sensor19.value]
    data_dict['sensor20']   = line[dataDescription.sensor20.value]
    data_dict['sensor21']   = line[dataDescription.sensor21.value]

    data_json = json.dumps(data_dict)
    print (data_json)
    print ("\n")

    myDeviceShadow.shadowUpdate( data_json, myShadowUpdateCallback, 5)
    #myDeviceShadow.shadowUpdate(
    #    '{"state":{"reported": '+ data_json +'}}',
    #    myShadowUpdateCallback, 5)
    line = rdfile.readline()
    time.sleep(10)

