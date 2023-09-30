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


class MILK_TYPE(Enum):
    whole = 0
    _1 = 1
    _2 = 2
    fat_free = 3
    almond = 4
    cashew = 5
    oat = 6

class BREAD_TYPE(Enum):
    whole_wheat = 0
    pumpernickel = 1
    rye = 2
    gluten_free = 3
 
class MEAT_TYPE(Enum):
  chicken = 0
  beef = 1
  turkey = 2
  ham = 3


@dataclass
class MILK:

  milk_type: MILK_TYPE = MILK_TYPE._2.value
  milk_quantity: float = 0
  
  def __init__ (self):
    pass

@dataclass
class BREAD:

  bread_type: BREAD_TYPE = BREAD_TYPE.whole_wheat.value
  bread_quantity: float = 0
  
  def __init__ (self):
    pass

@dataclass
class MEAT:

  meat_type: MEAT_TYPE = MEAT_TYPE.beef.value
  meat_quantity: float = 0
  
  def __init__ (self):
    pass

@dataclass
class BOTTLES:

  sprite: int = 0
  fanta: int = 0
  pepsi: int = 0
  mtn_dew: int = 0
  
  def __init__ (self):
    pass

@dataclass
class CANS:

  coke: int = 0
  bud_light: int = 0
  miller_lite: int = 0
  
  def __init__ (self):
    pass

@dataclass
class DRINKS:
  can: CANS
  bottle: BOTTLES

  def __init__ (self):
    pass

@dataclass
class VEGGIES:
  tomato: float = 0.0
  cucumber: float = 0.0
  pickle: float = 0.0
  jalapeno: float = 0.0
  mushroom: float = 0.0
  onion: float = 0.0

  def __init__ (self):
    pass


@dataclass
class Content:
  veggies: VEGGIES
  drinks: DRINKS
  milk: List[MILK]
  bread: List[BREAD]
  meat: List[MEAT]

  def __init__ (self):
    pass

@dataclass
class CustomOrder:
  """ Our message in native representation"""
  content: Content

  def __init__ (self):
    pass
  
  def dump (self):
    print ("Dumping contents of Custom Order")
    print ("  Content: {}".format (self.content))



