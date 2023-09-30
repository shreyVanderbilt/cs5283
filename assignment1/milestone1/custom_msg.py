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

@dataclass
class MILK:

  milk_type: Enum
  milk_quantity: float
  
  def __init__ (self):
    pass

@dataclass
class BREAD:

  bread_type: Enum
  bread_quantity: float
  
  def __init__ (self):
    pass

@dataclass
class MEAT:

  meat_type: Enum
  meat_quantity: float
  
  def __init__ (self):
    pass

@dataclass
class BOTTLES:

  sprite: int 
  fanta: int
  pepsi: int
  mtn_dew: int
  
  def __init__ (self):
    pass

@dataclass
class CANS:

  coke: int
  bud_light: int
  miller_lite: int 
  
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
  tomato: float
  cucumber: float
  pickle: float
  jalapeno: float
  mushroom: float
  onion: float

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



