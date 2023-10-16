# CS5383: Computer Networks - Programming Assignment #1

**Instructor**: Aniruddha Gokhale  
**Vanderbilt University, Fall 2023**  
**Team Members**: 
- Shrey Patel
- Nelson Torres
- Justin Sumner

## Introduction

This project is a part of the CS5383 course at Vanderbilt University for the Fall 2023 semester. The objective of this assignment is to create a client-server networking solution that leverages a custom Application Protocol. This protocol will operate on top of both gRPC and ZeroMQ communication frameworks. Serialization will be handled through two primary mechanisms - Protobuf and Flatbuffers.

Please follow the instructions below to set up and test the project.

## Screenshots

![Screenshot Description](URL_TO_SCREENSHOT1)
![Screenshot Description](URL_TO_SCREENSHOT2)

---

## Setup and Installation

1. **Clone the Repository**

```
git clone git@github.com:shreyVanderbilt/cs5283.git
```

2. **Navigate to the Project Directory**

```
cd cs5283
```
 

3. **Install Dependencies**

```sudo apt-get install python3-pip
pip3 install flatbuffers
pip3 install numpy
pip3 install zmq 
```

4. **Run the Application: Flatbuffer**
    1. Launch mininet
        ```
        sudo mn
        ```
    2. xterm h1
        ```
        xterm h1
        ```
    3. xterm h2
        ```
        xterm h2
        ```
    4. On h1 xterm
        1. Run "ifconfig" - Note the first inet value -> usually 10.0.0.1
            ```
            ifconfig
            ```
        2. Run the server
            ```
            python flatbufdemo_zmq.py -t server
            ```
    5. On h2 xterm
        1. Run the client
            1. 
            '''
            python flatbufdemo_zmq.py -i 1 --type client  --address 10.0.0.1 --iters 1
            '''
        2. Replace `10.0.0.1`` with inet value from 4-1
        3. Change "--iters 1" to how many orders you want to seralize and deseralize
    6. Check xterm h1 for order deseralization

5. **Run the Application: Protobuf**
    1. Server (h1):
        1. Run "ifconfig" - Note the first inet value -> usually 10.0.0.1
            ```
            ifconfig
            ```
        2. Run the server
            ```
            python protobufdemo_grpc_server.py
            ```
    2. Client (h2):
        1. run the client
            ```
            python protobufdemo_grpc_client.py --iters 2 --address 10.0.0.1 --type order
            ```
        2. Set type to order or health depending on type of message you want sent
        3. Change address to inet value and iters to number of orders/health request
