#  Author: Aniruddha Gokhale
#  Created: Fall 2021
#  (based on code developed for Distributed Systems course in Fall 2019)
#  Modified: Fall 2022 (changed packet name to not confuse with pub/sub Messages)
#
#  Purpose: demonstrate serialization of user-defined packet structure
#  using flatbuffers
#
#  Here our packet or message format comprises a sequence number, a timestamp,
#  and a data buffer of several uint32 numbers (whose value is not relevant to us)

import os
import sys

# this is needed to tell python where to find the flatbuffers package
# make sure to change this path to where you have compiled and installed
# flatbuffers.  If the python package is installed in your system wide files
# or virtualenv, then this may not be needed
sys.path.append(os.path.join (os.path.dirname(__file__), '/home/gokhale/Apps/flatbuffers/python'))
import flatbuffers    # this is the flatbuffers package we import
import time   # we need this get current time
import numpy as np  # to use in our vector field

import zmq   # we need this for additional constraints provided by the zmq serialization

from custom_msg import CustomOrder  # our custom message in native format
import OrderAppProto.BOTTLES as bottles   # this is the generated code by the flatc compiler
import OrderAppProto.BREAD as bread   # this is the generated code by the flatc compiler
import OrderAppProto.BREAD_TYPE as bread_type   # this is the generated code by the flatc compiler
import OrderAppProto.CANS as cans   # this is the generated code by the flatc compiler
import OrderAppProto.CONTENT as content   # this is the generated code by the flatc compiler
import OrderAppProto.DRINKS as drinks   # this is the generated code by the flatc compiler
import OrderAppProto.MEAT as meat   # this is the generated code by the flatc compiler
import OrderAppProto.MEAT_TYPE as meat_type   # this is the generated code by the flatc compiler
import OrderAppProto.MILK as milk   # this is the generated code by the flatc compiler
import OrderAppProto.MILK_TYPE as milk_type   # this is the generated code by the flatc compiler
import OrderAppProto.ORDER as order   # this is the generated code by the flatc compiler
import OrderAppProto.VEGGIES as veggies   # this is the generated code by the flatc compiler

# This is the method we will invoke from our driver program
# Note that if you have have multiple different message types, we could have
# separate such serialize/deserialize methods, or a single method can check what
# type of message it is and accordingly take actions.
def serialize (cm):
    # first obtain the builder object that is used to create an in-memory representation
    # of the serialized object from the custom message
    builder = flatbuffers.Builder (0);
    
    veggies.Start(builder)
    veggies.AddTomato(builder, cm.content.veggies.tomato)
    veggies.AddCucumber(builder, cm.content.veggies.cucumber)
    veggies.AddPickle(builder, cm.content.veggies.pickle)
    veggies.AddJalapeno(builder, cm.content.veggies.jalapeno)
    veggies.AddMushroom(builder, cm.content.veggies.mushroom)
    veggies.AddOnion(builder, cm.content.veggies.onion)
    order_veggies = veggies.End(builder)

    drinks.Start(builder)
    drinks.AddBottles(builder, bottles.CreateBOTTLES(builder, cm.content.drinks.bottle.sprite, cm.content.drinks.bottle.fanta, cm.content.drinks.bottle.pepsi, cm.content.drinks.bottle.mtn_dew))
    drinks.AddCans(builder, cans.CreateCANS(builder, cm.content.drinks.can.coke, cm.content.drinks.can.bud_light, cm.content.drinks.can.miller_lite))
    order_drinks = drinks.End(builder)


    milk_array = []
    for milk_item in cm.content.milk:
       milk.Start(builder)
       milk.AddMilkType(builder, milk_item.milk_type.value)
       milk.AddQuantity(builder, milk_item.milk_quantity)
       new_milk = milk.End(builder)
       milk_array.append(new_milk)

    bread_array = []
    for bread_item in cm.content.bread:
       bread.Start(builder)
       bread.AddBreadType(builder, bread_item.bread_type.value)
       bread.AddQuantity(builder, bread_item.bread_quantity)
       new_bread = bread.End(builder)
       bread_array.append(new_bread)

    meat_array = []
    for meat_item in cm.content.meat:
       meat.Start(builder)
       meat.AddMeatType(builder, meat_item.meat_type.value)
       meat.AddQuantity(builder, meat_item.meat_quantity)
       new_meat = meat.End(builder)
       meat_array.append(new_meat)

    content.StartMilkVector(builder, len(milk_array))
    for milk_i in reversed(milk_array):
      builder.PrependUOffsetTRelative(milk_i)
    order_milk = builder.EndVector()

    content.StartBreadVector(builder, len(bread_array))
    for bread_i in reversed(bread_array):
      builder.PrependUOffsetTRelative(bread_i)
    order_bread = builder.EndVector()

    content.StartMeatVector(builder, len(meat_array))
    for meat_i in reversed(meat_array):
      builder.PrependUOffsetTRelative(meat_i)
    order_meat = builder.EndVector()
    
    content.Start(builder)
    content.AddVeggies(builder, order_veggies)
    content.AddDrinks(builder, order_drinks)

    content.AddMilk(builder, order_milk)
    content.AddBread(builder, order_bread)
    content.AddMeat(builder, order_meat)

    order_content = content.End(builder)  # get the topic of all these fields

    order.Start(builder)
    order.AddContents(builder, order_content)
    serialized_msg = order.End(builder)

    # end the serialization process
    builder.Finish (serialized_msg)

    # get the serialized buffer
    buf = builder.Output ()

    # return this serialized buffer to the caller
    return buf

# serialize the custom message to iterable frame objects needed by zmq
def serialize_to_frames (cm):
  """ serialize into an interable format """
  # We had to do it this way because the send_serialized method of zmq under the hood
  # relies on send_multipart, which needs a list or sequence of frames. The easiest way
  # to get an iterable out of the serialized buffer is to enclose it inside []
  print ("serialize custom message to iterable list")
  return [serialize (cm)]
  
  
# deserialize the incoming serialized structure into native data type
def deserialize (buf):
    cm = CustomOrder();

    packet = order.ORDER.GetRootAs(buf, 0)

    # sequence number
    cm.content = packet.Contents()

    return cm
    
# deserialize from frames
def deserialize_from_frames (recvd_seq):
  """ This is invoked on list of frames by zmq """

  # For this sample code, since we send only one frame, hopefully what
  # comes out is also a single frame. If not some additional complexity will
  # need to be added.
  assert (len (recvd_seq) == 1)
  #print ("type of each elem of received seq is {}".format (type (recvd_seq[i])))
  print ("received data over the wire = {}".format (recvd_seq[0]))
  cm = deserialize (recvd_seq[0])  # hand it to our deserialize method

  # assuming only one frame in the received sequence, we just send this deserialized
  # custom message
  return cm
    
