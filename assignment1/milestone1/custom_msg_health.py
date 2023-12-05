# CS4283/5283: Computer Networks
# Instructor: Aniruddha Gokhale
# Created: Fall 2022
#
# Purpose: Define a native representation of a custom message format
#          that will then undergo serialization/deserialization
#

from typing import List
from dataclasses import dataclass
from enum import Enum


class STATUS(Enum):
    GOOD = 0
    BAD = 1
    _2 = 2

class DISPENSER(Enum):
    optimal = 0
    partial = 1
    blockage = 2
 

class HealthContent:
  dispenser: DISPENSER
  icemaker: int = 0
  lightbulb: STATUS
  fridge_temp: int = 32
  freeze_temp: int = 0
  sensor_status: STATUS

  def __init__ (self):
    pass

@dataclass
class CustomHealth:
  """ Our message in native representation"""
  content: HealthContent

  def __init__ (self):
    pass
  
  def dump_serialize (self):
    print ("Dumping contents of Custom Health")
    print ("  icemaker: {}; fridge_temp: {}; freeze_temp: {}; sensor_status: {}; ,lightbulb: {}; dispenser: {}".format (self.content.icemaker,self.content.fridge_temp,self.content.freeze_temp,self.content.sensor_status,self.content.lightbulb,self.content.dispenser))

  def dump_deserialize (self):
    print ("Dumping contents of Deserialized Custom Health")
    print ("  icemaker: {}; fridge_temp: {}; freeze_temp: {}; sensor_status: {}; ,lightbulb: {}; dispenser: {}".format (self.content.Icemaker(),self.content.FridgeTemp(),self.content.FreezeTemp(),self.content.SensorStatus(),self.content.Lightbulb(),self.content.Dispenser()))



