from random import randint
from time import strftime

class Compute(object):
    count = 0

    def __init__(self):
        self.count += 1
        self.object_type = 'I am a ' + self.__class__.__name__

    def ps(self):
        print "There are a lot of processes running"

    def echo(self,echoinput):
        print echoinput

    def virt_ip(self):
        return randint(1,100)

class Container(Compute):
    def __init__(self):
        self._status = "stopped"

    def start(self):
        self._status = "started"
        print "Container Started"

    def stop(self):
        self._status = "stopped"
        print "Container Stopped"

    @property
    def status(self):
        return self._status

class VM(Compute):
    def snapshot(self):
        self._snapshot_date = strftime("%H:%M:%S")
        print "snapshot taken"

    @property
    def snapshot_date(self):
        return self._snapshot_date

class Physical(Compute):
    def __init__(self):
        self.bios_boot_priority = "hdd"

    def __setattr__(self, name, value):
        if name == 'bios_boot_priority':
            if value not in ['usb', 'cd', 'hdd']:
                raise AttributeError("%s can't be set to %s" %(name, value))
                exit(1)
        super(Physical, self).__setattr__(name, value)

    def __getattr__(self, name):
        if name in ['virt_ip']:
            raise AttributeError('no such method')
        return super(Physical, self).__getattribute__(name)






