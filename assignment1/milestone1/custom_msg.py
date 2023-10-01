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
  
  def dump_serialize (self):
    print ("Dumping contents of Custom Order")
    print ("  Tomatos: {}; Cucmber: {}; Pickle: {}; Jalapeno: {}; ,Mushroom: {}; Onion: {}".format (self.content.veggies.tomato,self.content.veggies.cucumber,self.content.veggies.pickle,self.content.veggies.jalapeno,self.content.veggies.mushroom,self.content.veggies.onion))
    print ("  Coke can: {}; BUD LIGHT can: {}; Miller Lite can: {}".format( self.content.drinks.can.coke, self.content.drinks.can.bud_light, self.content.drinks.can.miller_lite))
    print ("  Sprite Bottle: {}; Fanta Bottle: {}; Pepsi Bottle: {}; MTN Dew Bottle: {}".format( self.content.drinks.bottle.sprite, self.content.drinks.bottle.fanta, self.content.drinks.bottle.pepsi, self.content.drinks.bottle.mtn_dew))
    print ("   ------ MEATS ------ ")
    for index, meat_i in enumerate(self.content.meat):
      print("     {}. Meat Type: {}; Meat Quantity: {}".format(index, meat_i.meat_type, meat_i.meat_quantity))
    print ("   ------ MILKS ------ ")
    for index, milk_i in enumerate(self.content.milk):
      print("     {}. Milk Type: {}; Milk Quantity: {}".format(index, milk_i.milk_type, milk_i.milk_quantity))
    print ("   ------ BREADS ------ ")
    for index, bread_i in enumerate(self.content.bread):
      print("     {}. Bread Type: {}; Bread Quantity: {}".format(index, bread_i.bread_type, bread_i.bread_quantity))

  def dump_deserialize (self):
    print ("Dumping contents of Deserialized Custom Order")
    print ("  Tomatos: {}; Cucmber: {}; Pickle: {}; Jalapeno: {}; ,Mushroom: {}; Onion: {}".format (self.content.Veggies().Tomato(),self.content.Veggies().Cucumber(),self.content.Veggies().Pickle(),self.content.Veggies().Jalapeno(),self.content.Veggies().Mushroom(), self.content.Veggies().Onion() ))
    print ("  Coke can: {}; BUD LIGHT can: {}; Miller Lite can: {}".format( self.content.Drinks().Cans().Coke(), self.content.Drinks().Cans().BudLight(), self.content.Drinks().Cans().MillerLite()))
    print ("  Sprite Bottle: {}; Fanta Bottle: {}; Pepsi Bottle: {}; MTN Dew Bottle: {}".format( self.content.Drinks().Bottles().Sprite(), self.content.Drinks().Bottles().Fanta(), self.content.Drinks().Bottles().Pepsi(), self.content.Drinks().Bottles().MtnDew()))
    print ("   ------ MEATS ------ ")
    for index in range(self.content.MeatLength()):
      meat_i = self.content.Meat(index)
      print("     {}. Meat Type: {}; Meat Quantity: {}".format(index, meat_i.MeatType(), meat_i.Quantity()))
    print ("   ------ MILKS ------ ")
    for index in range(self.content.MilkLength()):
      milk_i = self.content.Milk(index)
      print("     {}. Milk Type: {}; Milk Quantity: {}".format(index, milk_i.MilkType(), milk_i.Quantity()))
    print ("   ------ BREADS ------ ")
    for index in range(self.content.BreadLength()):
      bread_i = self.content.Bread(index)
      print("     {}. Bread Type: {}; Bread Quantity: {}".format(index, bread_i.BreadType(), bread_i.Quantity()))



