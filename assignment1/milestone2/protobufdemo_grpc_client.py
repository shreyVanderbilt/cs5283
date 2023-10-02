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
        veggies.tomato = 1.0
        veggies.jalapeno = 1.0
        veggies.onion = 1.0

        drinks = spb.Drinks()
        cans = spb.Cans()
        bottles = spb.Bottles()

        cans.bud_light = 1
        bottles.sprite = 1
        drinks.bottles.ParseFromString(bottles.SerializeToString())
        drinks.cans.ParseFromString(cans.SerializeToString())

        bread1 = spb.Bread()
        bread1.bread_type = spb.Bread_Type.rye
        bread1.quantity = 1

        bread2 = spb.Bread()
        bread2.bread_type = spb.Bread_Type.whole_wheat
        bread2.quantity = 2

        meat1 = spb.Meat()
        meat1.meat_Type = spb.Meat_Type.beef
        meat1.quantity = 1

        milk1 = spb.Milk()
        milk1.milk_type = spb.Milk_Type.almond
        milk1.quantity = 1

        content = spb.Content()
        content.veggies.ParseFromString(veggies.SerializeToString())
        content.drinks.ParseFromString(drinks.SerializeToString())
        content.milk.append(milk1)
        content.bread.append(bread1)
        content.bread.append(bread2)
        content.meat.append(meat1)

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
