from random import randint
from time import strftime
from traceback import print_exc

print "please run --> "
print "from example import *"

# main class has common methods and attributes
class Compute(object):

    # need this to return attribute as unquoted string
    @property
    def object_type(self):
        print '%s' % ('I am a ' + self.__class__.__name__)

    # printing ps() task
    def ps(self):
        print '%s' % ("There are a lot of processes running")

    # printing echo(something) task
    def echo(self,echoinput):
        print echoinput

    # returning random integer 1-100, in case we called inside Physical child will simulate not-exists error
    def virt_ip(self):
        if self.__class__.__name__ == 'Physical':
            raise AttributeError('no such method')
        return randint(1,100)

# Container class, inheriting from common class
class Container(Compute):

    # class variable to count instances of object
    instance_count = 0

    # need this to return attribute as unquoted string
    # status attribute will not be set directly (read-only)
    @property
    def status(self):
        print '%s' % (self._status)

    def __init__(self):
        # incrementing counter class variable
        Container.instance_count += 1
        # status shouldn't be set directly, using _status to keep this state
        self._status = "stopped"

    def start(self):
        self._status = "started"
        print '%s' % ("Container Started")

    def stop(self):
        self._status = "stopped"
        print '%s' % ("Container Stopped")

# VM class, inheriting from common class
class VM(Compute):

    instance_count = 0

    def __init__(self):
        VM.instance_count += 1


    def snapshot(self):
        # using strftime method from time module
        self._snapshot_date = strftime("%Y-%m-%d %H:%M:%S")
        print '%s' % ("snapshot taken")

    # set read-only snapshot_date attribute
    @property
    def snapshot_date(self):
        print '%s' % (self._snapshot_date)

# custom exception class, inheriting from general Exception class
class EInvalidBootObject(Exception):
    def __init__(self):
        message = "valid values: usb, cd, hdd"
        # appending custom message to original exception message
        super(EInvalidBootObject, self).__init__(message)

# Physical class, inheriting from common class
class Physical(Compute):

    instance_count = 0

    # we will catch original attempt to set bios_boot_priority attribute later
    @property
    def bios_boot_priority(self):
        print '%s' % (self._bios_boot_priority)

    def __init__(self):
        Physical.instance_count += 1
        # initialize default _bios_boot_priority which will be return as bios_boot_priority
        self._bios_boot_priority = 'hdd'

    # catching attempt to set bios_boot_priority, then validate value
    def __setattr__(self, name, value):
        try:
            # validate user input
            if name == 'bios_boot_priority':
                if value not in ['usb', 'cd', 'hdd']:
                    # raise custom exception defined above
                    raise EInvalidBootObject
            # if value was ok then set _bios_boot_priority which will be returned as bios_boot_priority
            super(Physical, self).__setattr__("_bios_boot_priority", value)
        # except custom exception defined above
        except EInvalidBootObject:
            print_exc()






