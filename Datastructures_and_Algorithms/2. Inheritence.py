from enum import Enum

class SecurityDevice:
    def __init__(self, active):
        self.active = active

    #create the method 
    def reset(self):
        print("Resetting...")
        self.active = True
        
#inheritance - The Sensor class is inheriting attributes from the SecurityDevice class. 
class Sensor(SecurityDevice):
    def __init__(self, active, silent, distance):
        self.active = active
        self.silent = silent
        self.distance = distance


class Position: 
    def __init__(self, pan, tilt, zoom):
        self.pan = pan 
        self.tilt = tilt
        self.zoom = zoom 
    
    def __str__(self):
        return f"Pan: {str(self.pan}. Tilt: {str(self.tilt)}. Zoom: {str(self.zoom})}."
        

security_device = SecurityDevice(True)
print(security_device)

sensor = Sensor(False, 30)
print(sensor)
sensor.reset()
print(sensor.active)

print(type(sensor))

#check if sensor is a subclass of SecurityDevice 
print(issubclass(sensor,SecurityDevice))
