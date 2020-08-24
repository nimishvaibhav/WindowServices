import wmi
#import psutil

services = ['Bonjour Service', 'avast! Antivirus', 'iPod Service']

#Connec to Windows
c = wmi.WMI()

#to check the state of the service
def checkServices():
    for service in c.Win32_Service():
        #print(service)
        if service.Name in services:
            print(service.Name + ' -- ' + service.State + ' -- ' + service.StartMode +' -- ' + service.SystemName)

#to check and restart the service
def restartServices():
    for service in c.Win32_Service():
        if service.Name in services:
            if service.State == 'Running':
                print(service.Name + ' is Running')
            else:
                print(service.Name + ' is Stopped')
                result = service.StartService()
                print(result)
                print(service.Name + ' -- ' + service.State)

checkServices()
restartServices()

