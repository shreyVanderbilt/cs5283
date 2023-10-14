#  Author: Aniruddha Gokhale
#  Created: Fall 2023
#
#  Purpose: demonstrate serialization of a user-defined data structure using
#  Protocol Buffers combined with gRPC. Note that here we
#  are more interested in how a serialized packet gets sent over the network
#  and retrieved. To that end, we really don't care even if the client and
#  server were both on the same machine or remote to each other.

# This one implements the client functionality
#

# Note that this code mimics what we did with FlatBufs+ZeroMQ but this time
# we mix Protocol Buffers and gRPC

# The different packages we need in this Python driver code
import os
import sys
import time  # needed for timing measurements and sleep

import random  # random number generator
import argparse  # argument parser

import logging

import grpc   # for gRPC

# import generated packages
import schema_pb2 as spb
import schema_pb2_grpc as spb_grpc

##################################
#        Driver program
##################################

def driver (iters, port, address, type):

  print ("Driver program: Num Iters = {}, Port = {}, Address = {}".format (iters, port, address, type))

  if type == 'order':
     
    print ("Driver program: create handle to the client and then run the code -- ORDER")
    try:

      # Use the insecure channel to establish connection with server
      print ("Instantiate insecure channel")
      channel = grpc.insecure_channel (str(address) + ":" + str (port))

      print ("Obtain a proxy object to the server")
      stub = spb_grpc.OrderServiceStub(channel)

      # now send the serialized custom message for the number of desired iterations
      print ("Allocate the Request object that we will then populate in every iteration")
      req = spb.Order()

      for i in range (iters):
        # for every iteration, let us fill up our custom message with some info
        veggies = spb.Veggies()
        veggies.tomato = float(random.randint(0, 10)) + random.randint(0, 9) / 10.0
        veggies.jalapeno = float(random.randint(0, 10)) + random.randint(0, 9) / 10.0
        veggies.onion = float(random.randint(0, 10)) + random.randint(0, 9) / 10.0
        veggies.cucumber = float(random.randint(0, 10)) + random.randint(0, 9) / 10.0
        veggies.pickle = float(random.randint(0, 10)) + random.randint(0, 9) / 10.0
        veggies.jalapeno = float(random.randint(0, 10)) + random.randint(0, 9) / 10.0

        drinks = spb.Drinks()
        cans = spb.Cans()
        bottles = spb.Bottles()

        cans.coke = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)
        cans.bud_light = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)
        cans.miller_lite = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        bottles.sprite = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)
        bottles.fanta = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)
        bottles.pepsi = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)
        bottles.mtn_dew = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)
    
        drinks.bottles.ParseFromString(bottles.SerializeToString())
        drinks.cans.ParseFromString(cans.SerializeToString())

        milk_ele1 = spb.Milk()
        milk_ele1.milk_type = int(random.randint(0, 6))
        milk_ele1.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        milk_ele2 = spb.Milk()
        milk_ele2.milk_type = int(random.randint(0, 6))
        milk_ele2.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        milk_ele3 = spb.Milk()
        milk_ele3.milk_type = int(random.randint(0, 6))
        milk_ele3.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        bread_ele1 = spb.Bread()
        bread_ele1.bread_type = int(random.randint(0, 4))
        bread_ele1.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        bread_ele2 = spb.Bread()
        bread_ele2.bread_type = int(random.randint(0, 4))
        bread_ele2.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        meat_ele1 = spb.Meat()
        meat_ele1.meat_Type = int(random.randint(0, 4))
        meat_ele1.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        meat_ele2 = spb.Meat()
        meat_ele2.meat_Type = int(random.randint(0, 4))
        meat_ele2.quantity = int(random.randint(0, 10) + random.randint(0, 9) / 10.0)

        content = spb.Content()
        content.veggies.ParseFromString(veggies.SerializeToString())
        content.drinks.ParseFromString(drinks.SerializeToString())
        content.milk.extend([milk_ele1, milk_ele2, milk_ele3])
        content.bread.extend([bread_ele1, bread_ele2])
        content.meat.extend([meat_ele1,meat_ele2])

        req.content.ParseFromString(content.SerializeToString())

        print ("-----Iteration: {} contents of message before sending\n{} ----------".format (i, req))

        # now let the client send the message to its server part
        print ("Peer client sending the serialized message")
        start_time = time.time ()
        resp = stub.method (req)
        end_time = time.time ()
        print ("sending/receiving took {} secs".format (end_time-start_time))

        print (" Response recieved: ", resp)

        # sleep a while before we send the next serialization so it is not
        # extremely fast
        time.sleep (0.050)  # 50 msec

    except:
      return
  else:
    
    print ("Driver program: create handle to the client and then run the code -- HEALTH")
    try:

      # Use the insecure channel to establish connection with server
      print ("Instantiate insecure channel")
      channel = grpc.insecure_channel (str(address) + ":" + str (port))

      print ("Obtain a proxy object to the server")
      stub = spb_grpc.HealthServiceStub(channel)

      # now send the serialized custom message for the number of desired iterations
      print ("Allocate the Request object that we will then populate in every iteration")
      req = spb.Health()

      for i in range (iters):
        # for every iteration, let us fill up our custom message with some info

        healthContent = spb.Health_Content()
        healthContent.freeze_temp = 1
        healthContent.fridge_temp = 33
        healthContent.icemaker = 1
        healthContent.dispenser = spb.Dispenser.partial
        healthContent.sensor_status = spb.Status.bad
        healthContent.lightbulb = spb.Status.good

        req.healthContent.ParseFromString(healthContent.SerializeToString())

        print ("-----Iteration: {} contents of message before sending\n{} ----------".format (i, req))

        # now let the client send the message to its server part
        print ("Peer client sending the serialized message")
        start_time = time.time ()
        resp = stub.method (req)
        end_time = time.time ()
        print ("sending/receiving took {} secs".format (end_time-start_time))

        print (" Response recieved: ", resp)

        # sleep a while before we send the next serialization so it is not
        # extremely fast
        time.sleep (0.050)  # 50 msec
    except:
      return
     

  
##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-i", "--iters", type=int, default=10, help="Number of iterations to run (default: 10)")
    parser.add_argument ("-p", "--port", type=int, default=5577, help="Port where the server part of the peer listens and client side connects to (default: 5577)")
    parser.add_argument ("-a", "--address", default="localhost", help="IP address")
    parser.add_argument ("-t", "--type", default="order", help="Request type. order/health")

    # parse the args
    args = parser.parse_args ()

    return args
    
#------------------------------------------
# main function
def main ():
  """ Main program """

  print("Demo program for Protocol Buffers with gRPC serialization/deserialization")

  # first parse the command line args
  parsed_args = parseCmdLineArgs ()
    
  # start the driver code
  driver (parsed_args.iters, parsed_args.port, parsed_args.address, parsed_args.type)

#----------------------------------------------
if __name__ == '__main__':
    main ()
