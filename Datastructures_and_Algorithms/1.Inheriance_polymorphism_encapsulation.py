# Inheritence - attributes inheritd from parent class
#ex. class Camera extends SecurityDevice

    

#polymorphism - treating a bunch of diffent clases as the base class, and having an option to invoke a more method or access a more specefic attribute inside the new class

camera = Camera()
sensor =  Sensor()

security_devices = [camera, sensor]

for security-device in security_devices:
    security_devices.activate()



#ecapsualtion - 
#properties use get and set methods 

camera = camera
camera.serial_number = "ABC-123"

