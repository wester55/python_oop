from random import randint
from time import strftime
from traceback import print_exc

class Compute(object):

    @property
    def object_type(self):
        print '%s' % ('I am a ' + self.__class__.__name__)

    def ps(self):
        print '%s' % ("There are a lot of processes running")

    def echo(self,echoinput):
        print echoinput

    def virt_ip(self):
        if self.__class__.__name__ == 'Physical':
            raise AttributeError('no such method')
        return randint(1,100)

class Container(Compute):

    instance_count = 0

    @property
    def status(self):
        print '%s' % (self._status)

    def __init__(self):
        Container.instance_count += 1
        self._status = "stopped"

    def start(self):
        self._status = "started"
        print '%s' % ("Container Started")

    def stop(self):
        self._status = "stopped"
        print '%s' % ("Container Stopped")

class VM(Compute):

    instance_count = 0

    def __init__(self):
        VM.instance_count += 1

    def snapshot(self):
        self._snapshot_date = strftime("%Y-%m-%d %H:%M:%S")
        print '%s' % ("snapshot taken")

    @property
    def snapshot_date(self):
        print '%s' % (self._snapshot_date)

class EInvalidBootObject(Exception):
    def __init__(self):
        message = "valid values: usb, cd, hdd"
        super(EInvalidBootObject, self).__init__(message)

class Physical(Compute):

    instance_count = 0

    @property
    def bios_boot_priority(self):
        print '%s' % (self._bios_boot_priority)

    def __init__(self):
        Physical.instance_count += 1
        self._bios_boot_priority = 'hdd'

    def __setattr__(self, name, value):
        try:
            if name == 'bios_boot_priority':
                if value not in ['usb', 'cd', 'hdd']:
                    raise EInvalidBootObject
            super(Physical, self).__setattr__("_bios_boot_priority", value)
        except EInvalidBootObject:
            print_exc()






