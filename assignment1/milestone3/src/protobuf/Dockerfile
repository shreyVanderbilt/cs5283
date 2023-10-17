# Author: Aniruddha Gokhale
# Vanderbilt University
# Created: Fall 2023
#
# For Computer Networks course
#
# This dockerfile creates an image to run our Python program
# that encodes the Protocol Buffer + gRPC combo.  
# We are packaging both the client and server files in one docker
# file and creating just one image out of it so that we don't have
# to create multiple images with such a trivial difference between
# the two
#
# The FROM keyword tells the build process what the base image is
# from which to start building. We use Ubuntu 22:04
# jammy or 22.04 tag can be used. As of today, "latest" tag also points
# to this tag
FROM ubuntu:jammy 
#
# The RUN directive is used to customize the image with
# whatever packages we want to install as well as any other
# modifications, configurations we want to do
#
# Install the needed packages. The "-y" eliminates the interactive response
# We first install the key packages we need like Java and Python3
RUN apt -y update && apt install -y default-jdk python3
#
# Then we install Pip3 upgrading it to the latest version in case any python
# packages are needed to be installed
RUN apt install -y python3-dev python3-pip
RUN python3 -m pip install --upgrade pip
#
# Now we install some utilities just in case we need to debug from
# inside the pod/container.
RUN apt install -y net-tools wget dnsutils iputils-ping iputils-tracepath iputils-arping iputils-clockdiff
#
# Install the Protocol Buffer package and GRPC
RUN apt install -y protobuf-compiler-grpc
#
RUN python3 -m pip install --upgrade grpcio grpcio-tools
#
#
# Tell Docker what is going to be our working directory instead of the / directory
# by default. By specifying the directory, if one does not exist, it will be created.
WORKDIR /work
#
# Now let us keep our python program inside this image.
# For this we use the COPY directive that copies code from host to this image
# into the working directory
COPY milestone2/protobufdemo_grpc_client.py .
COPY milestone2/protobufdemo_grpc_server.py .
COPY milestone2/schema_pb2_grpc.py .
COPY milestone2/schema_pb2.py .
COPY milestone2/schema_pb2.pyi .
COPY milestone2/schema.proto .
#
#
# If we were to run Docker images natively, then one could provide the
# command to run when the docker image is executed. But here we skip
# that step and instead let K8s take care of it

