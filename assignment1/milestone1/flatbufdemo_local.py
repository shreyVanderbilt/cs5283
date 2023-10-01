#  Author: Aniruddha Gokhale
#  Created: Fall 2021
#  Modified: Fall 2022 (for Computer Networking course)
#
#  Purpose: demonstrate serialization of a user-defined data structure using
#  FlatBuffers
#
#  Here our custom message format comprises a sequence number, a timestamp, a name,
#  and a data buffer of several uint32 numbers (whose value is not relevant to us) 

# The different packages we need in this Python driver code
import os
import sys
import time  # needed for timing measurements and sleep

import random  # random number generator
import argparse  # argument parser

## the following are our files
from custom_msg import CustomOrder  # our custom message in native format
from custom_msg import MILK  # our custom message in native format
from custom_msg import MEAT  # our custom message in native format
from custom_msg import BREAD  # our custom message in native format
from custom_msg import DRINKS  # our custom message in native format
from custom_msg import BOTTLES  # our custom message in native format
from custom_msg import CANS  # our custom message in native format
from custom_msg import VEGGIES  # our custom message in native format
from custom_msg import MILK_TYPE
from custom_msg import BREAD_TYPE
from custom_msg import MEAT_TYPE
from custom_msg import Content

import serialize_flatbuf as sz  # this is from the file serialize.py in the same directory

##################################
#        Driver program
##################################

def driver (name, iters, vec_len):

  print ("Driver program: Name = {}, Num Iters = {}, Vector len = {}".format (name, iters, vec_len))
  cm = CustomOrder()
  # now publish our information for the number of desired iterations
  for i in range (iters):

    veggies = VEGGIES()
    veggies.tomato = 1.0
    veggies.jalapeno = 1.0
    veggies.onion = 2.0
    
    drinks = DRINKS()
    bottles = BOTTLES()
    bottles.sprite = 2
    cans = CANS()
    cans.bud_light = 1
    drinks.bottle = bottles
    drinks.can = cans

    milk_ele1 = MILK()
    milk_ele1.milk_type = MILK_TYPE.almond
    milk_ele1.milk_quantity = 1.2

    milk_ele2 = MILK()
    milk_ele2.milk_type = MILK_TYPE.cashew
    milk_ele2.milk_quantity = 2.0
    
    milk_array = [milk_ele1, milk_ele2]

    bread_ele1 = BREAD()
    bread_ele1.bread_type = BREAD_TYPE.pumpernickel
    bread_ele1.bread_quantity = 2.0

    bread_ele2 = BREAD()
    bread_ele2.bread_type = BREAD_TYPE.rye
    bread_ele2.bread_quantity = 1.0
    
    bread_array = [bread_ele1, bread_ele2]

    meat_ele1 = MEAT()
    meat_ele1.meat_type = MEAT_TYPE.beef
    meat_ele1.meat_quantity = 2.4
    
    meat_array = [meat_ele1]

    order_content = Content
    order_content.veggies = veggies
    order_content.drinks = drinks
    order_content.milk = milk_array
    order_content.bread = bread_array
    order_content.meat = meat_array

    cm.content = order_content
    
    print ("-----Iteration: {} contents of message before serializing ----------".format (i))
    cm.dump_serialize ()
        
    # here we are calling our serialize method passing it
    # the iteration number, the topic identifier, and length.
    # The underlying method creates some dummy data, fills
    # up the data structure and serializes it into the buffer
    print ("serialize the message")
    start_time = time.time ()
    buf = sz.serialize (cm)
    end_time = time.time ()
    print ("Serialization took {} secs".format (end_time-start_time))

    # now deserialize and see if it is printing the right thing
    print ("deserialize the message")
    start_time = time.time ()
    cm = sz.deserialize (buf)
    end_time = time.time ()
    print ("Deserialization took {} secs".format (end_time-start_time))

    print ("------ contents of message after deserializing ----------")
    cm.dump_deserialize()

    # sleep a while before we send the next serialization so it is not
    # extremely fast
    time.sleep (0.050)  # 50 msec


##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-i", "--iters", type=int, default=10, help="Number of iterations to run (default: 10)")
    parser.add_argument ("-l", "--veclen", type=int, default=20, help="Length of the vector field (default: 20; contents are irrelevant)")
    parser.add_argument ("-n", "--name", default="FlatBuffer Local Demo", help="Name to include in each message")
    # parse the args
    args = parser.parse_args ()

    return args
    
#------------------------------------------
# main function
def main ():
    """ Main program """

    print("Demo program for Flatbuffer serialization/deserialization")

    # first parse the command line args
    parsed_args = parseCmdLineArgs ()
    
   # start the driver code
    driver (parsed_args.name, parsed_args.iters, parsed_args.veclen)

#----------------------------------------------
if __name__ == '__main__':
    main ()
