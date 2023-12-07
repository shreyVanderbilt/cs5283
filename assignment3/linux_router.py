#!/usr/bin/python
#
# CS/ECE 4383/5383: Computer Networks
# Author: Aniruddha Gokhale
# Created: Fall 2023
#
#  This is the Linux Router (same as from examples directory)
#
# Run this program under "sudo" mode
#

import os              # OS level utilities
import sys
import argparse   # for command line parsing

# Many of the packages that need to be imported. See
# https://mininet.org/api/index.html
from mininet.node import Node

# other utility classes
from mininet.log import setLogLevel, info

########################################
# This router class is as before (from examples directory)
########################################
class LinuxRouter (Node):
  def config (self, **params):
    info ("Linux Router config for router " + self.name + "\n")
    super ().config (**params)
    self.cmd ('sysctl net.ipv4.ip_forward=1')

  def terminate (self):
    info ("Linux Router terminate for router " + self.name + "\n")
    self.cmd ('sysctl net.ipv4.ip_forward=0')
    super ().terminate ()

