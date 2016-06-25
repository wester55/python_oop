class Compute:
    count = 0
    def __init__(self):
        Compute.count += 1

    def ps(self):
        print "There are a lot of processes running"

    def echo(self,echoinput):
        print echoinput

    def object_type(self):
        print "I am a " + Compute.__name__


class Container(Compute):
   def __init__(self):
      pass

class VM(Compute):
   def __init__(self):
      pass

class Physical(Compute):
   def __init__(self):
      pass




