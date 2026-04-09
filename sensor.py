#sensor.py
import random as r

class sensor:
    """
    Base sensor class.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        
    def read(self) -> float:
        return 0.0 # to overwrite...
    
#Inheritance
class Temperaturesensor(sensor):
   """
   simulated temp sensor.
   """
   def __init__( self, name: str) ->None:
       super(). __init__(name)
       
   def read(self) -> float: # over written sensor. read()
        return round(r.uniform(20.0, 30.0), 2)
    
class lightsensor(sensor):
    """
    simulated light sensor.
    """
    def read(self) -> float: #overwrite..
        return round(r.uniform(0,100), 2)