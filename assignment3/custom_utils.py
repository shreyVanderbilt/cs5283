#
# CS/ECE 4383/5383: Computer Networks
# Author: Aniruddha Gokhale
# Created: Fall 2023
#
#  This comprises utility methods
#


################################
#  Retrieve diff parts of a CIDRerized IP address
################################

def IP_components (cidr_ip):
  # first get the ip address from the CIDR form
  # There are several methods in mininet/utils.py file that could be used
  # but here, I just created my own way of doing things.
  #
  # First, get the a.b.c.d form out of the a.b.c.d/N format.
  ip_parts = cidr_ip[0:cidr_ip.index ("/")].split (".")
    
  # next, get the CIDR prefix len i.e., the /N part
  prefix_len = cidr_ip[cidr_ip.index ("/"):]   # get the /N part
  
  # since the split method created a list, we combine it to form the a.b.c.d
  # notation.
  # This logic is based on the premise that we are only concerned with the
  # last octet and which should be zero
  ip_prefix = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."

  return ip_prefix, prefix_len, ip_parts[3]

