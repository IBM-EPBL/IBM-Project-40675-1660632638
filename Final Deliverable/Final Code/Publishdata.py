import wiotp.sdk.device
import time
import random
#import randint as ri
myconfiq ={
    "identity":{
        "orgid":"8slgz2",
        "typeId":"sprint1type",
        "deviceId":"sprint1id"
        },
    "auth":{
        "token":"use-token-auth"
        }
    }
def myCommandCallback(cmd):
    print("received cmd:",cmd)
def logData2cloud(location, temperature, visibility):
    client=wiotp.sdk.devicc.DcviccClient(config=myconfig,logHandlcra=None)
    client.connect()
    client.publishEvent(eventId-"status",msgFormat-"json",data-{
        "temperature":ri(28,35),
        "visibility":ri(56,78),
        "location":"Chennai,IN"
        },qoS=0,onPublish=None)
    Client.commandCallback-myCommandCallback
    client.disconnect()
    time.sleep(1)
