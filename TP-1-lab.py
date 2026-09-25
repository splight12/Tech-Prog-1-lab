import os  # noqa: I001
import platform as pl
import getpass
import psutil as ps

data =  {
    'user': getpass.getuser(),
    'architecture': pl.architecture()[0],
    'system': pl.system()
}

if data['system'] == 'Linux':
    ...
print(data)


'''
сеть psutil
wifi ssid
ip
arp cache
'''