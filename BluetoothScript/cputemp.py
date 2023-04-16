#!/usr/bin/python3

import dbus
from promisio import promisify
from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor
import asyncio
import time
from multiprocessing import Process
import threading
#from gpiozero import CPUTemperature

#currently just keep on adding descruptors until 

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 5000
CUSTOM_SERVICE_ID = '4eb83bc6-1a30-40d8-97c3-001632596808' 
CUSTOM_CHARA_ID =   'd55372ef-ccde-4419-80fa-42fef70511c9'
CUSTOM_DESC_ID =    'b5a423XX-XXX4-f393-00a9-e50e24dcca9e'
                    #0123456789ABCDEF
EMPTY_ID = 'b5a423XX-XXX4-f393-00a9-e50e24dcca9e'
EMPTY_IDTest = '222222XX-XXX2-2222-2222-000000000000'
ID_iterable = 111111111111

class customDescriptor(Descriptor):
    outgoingMove = "a7-a60"
    def __init__(self, characteristic, move):
        global ID_iterable
        ID_iterable = ID_iterable + 1
        TempID = EMPTY_ID[0:6] + move + EMPTY_ID[12:24] + str(ID_iterable)
        Descriptor.__init__(self, TempID, ['read', 'write'], characteristic)
        
    def ReadValue(self, options):
        value = dbus.Array([])
        for b in outgoingMove:
            value.append(dbus.Byte(b.encode()))
        return value
    
    def setMove(self, move):
            ID_iterable += 1
            TempID = EMPTY_ID[0:6] + move + str(ID_iterable)
            #TempID[4:9] = move
            print(TempID)
            self.SelfClean()
            Descriptor.__init__(self, TempID, ['read', 'write'], characteristic)
            #self.set_uuid(TempID)

@promisify
async def returnVal():
    return "test"

class customCharacteristic(Characteristic):
    outgoingMove = "e7-e6"
    incomingMove = ""
    value = [dbus.Byte('g'.encode())]
    def __init__(self, index, service, move):
        Characteristic.__init__(self, CUSTOM_CHARA_ID, ['read', 'write', 'notify'], service)
        self.add_descriptor(customDescriptor(self, move)) #May want to modify to be tied to service instead of a local var
        Characteristic.value = [dbus.Byte('g'.encode())]
        self.value = [dbus.Byte('g'.encode())]
        #self.notifying = True
    
    def newDescriptor(self, move):
            self.add_descriptor(customDescriptor(self, move))
    
    def StartNotify(self):
        if self.notifying:
            return
        self.notifying = True
        
    
    def ReadValue(self, options):
        value = dbus.Array()
        for b in outgoingMove:
            value.append(dbus.Byte(b.encode()))
        print("testing")
        #return value
    
    def WriteCharacteristicValue(self, value, options):
        global CUSTOM_DESC_ID
        print("test")
        print(value)
        incomingMove = "".join([str(v) for v in value])
        print(incomingMove)
    
    def WriteValue(self, value, options):
        global CUSTOM_DESC_ID
        print("test")
        print(value)
        incomingMove = "".join([str(v) for v in value])
        print(incomingMove)
        #self.descriptors.clear()
        #print(self.descriptors)
        #CUSTOM_DESC_ID = 'd7d60000-b5a3-f393-00a9-e50e24dcca9e'
        #self.add_descriptor(customDescriptor(self))
        #self.descriptors[0].uuid = 'd7d60000-b5a3-f393-00a9-e50e24dcca9e'
        #print("sending")
        #print(self.descriptors[0].uuid)
        #self.PropertiesChanged("org.bluez.GattCharacteristic1", {'Value' : dbus.Byte(self.descriptors[0].uuid.encode())}, [])
        #self.PropertiesChanged("org.bluez.GattCharacteristic1", {'Value' : value}, [])
        #return returnVal()
        

class customService(Service):
    def __init__(self, index, move):
        Service.__init__(self, index, CUSTOM_SERVICE_ID, True)
        self.add_characteristic(customCharacteristic(0, self, move))
        
class customAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("Smart Chess Board")
        self.include_tx_power = False
        self.add_service_uuid(CUSTOM_SERVICE_ID)
        #self.add_service(CUSTOM_SERVICE_ID)
        
    def updateAdvertisement(self):
            self.clearServices()
            self.add_service_uuid(CUSTOM_SERVICE_ID)

'''
async def watcherTesting(app, move, sleep):
        print("watcherTesting 1")
        await asyncio.sleep(sleep)
        print("watcherTesting 5")
        app.services[0].characteristics[0].descriptors[0].setMove(move)
        print(app.services[0].characteristics[0].descriptors[0].uuid)
     
async def appTesting(app):
        print("appTesting 1")
        app.run()
   
async def waitTesting(app):
        print("waitTesting 1")
        checkTask = asyncio.create_task(watcherTesting(app, 'a3-a40', 5))
        print("waitTesting 2")
        apptask = asyncio.create_task(appTesting(app))
        print("waitTesting 3")
        await apptask
        print("waitTesting 4")
        await checkTask
        print("waitTesting 5")
'''

def runFunction(app):
        app.run()

def checkerFunction(app, adv, move):
        print("Check 1")
        #adv.release()
        #adv = customAdvertisement(0)
        #adv.register()
        app.quit()
        app.unregister()
        adv.unregister()
        print("Check 1.5")
        #app.clear_service()
        print("Check 2")
        #app.GetManagedObjects()
        app.services[0].characteristics[0].newDescriptor('a7-a60')
        #app.add_service(customService(0, 'a7-a60'))
        app.register()
        #adv2 = customAdvertisement(0)
        #adv2.register()
        #adv.updateAdvertisement()
        adv.register()
        print("Check 3")
        print(app.services[0].characteristics[0].descriptors[-1].uuid)
        #print(adv.get_properties())
        app.run()


app = Application()
app.clear_service()
app.add_service(customService(0, 'e7-e60'))
app.register()
print(app.services[0].uuid)
#app.services[0].characteristics[0].descriptors[0].setMove('e7-e60')
print(app.services[0].characteristics[0].descriptors[0].uuid)
adv = customAdvertisement(0)
adv.register()

'''
p1 = Process(target=checkerFunction(app, 'a3-a50'))
p2 = Process(target=runFunction(app))
p2.start()
p1.start()
p1.join()
p2.join()
'''

#t1 = threading.Thread(target= lambda: checkerFunction(app, 'a3-a50'))
#t2 = threading.Thread(target=runFunction(app))
#t2.start()
#t1.start()

t1 = threading.Timer(30, lambda: checkerFunction(app, adv, 'a7-a60'))
t2 = threading.Thread(target=lambda: runFunction(app))
t1.start()
t2.start()

#asyncio.run(waitTesting(app))

# Want to be able to change the bluetooth uuid while the loop is running (after the advertisement is registered)
# In order to do this, we need to have a program running in paralel called before app.run() and runs in the background
# To run asynchronously i need to check continuously for whenever the physical player makes a move, 

#try:
#    app.run()
#except KeyboardInterrupt:
#    app.quit()
