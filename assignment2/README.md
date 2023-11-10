# CS5383: Computer Networks - Programming Assignment #2

**Instructor**: Aniruddha Gokhale  
**Vanderbilt University, Fall 2023**  
**Team Members**: 
- Shrey Patel
- Nelson Torres
- Justin Sumner

# Milestone 1

## Set Up VMs on Chameleon Cloud
- VM named `ol_team4_vm1` set up on Chameleon Cloud.
- VM named `ol_team4_vm2` set up on Chameleon Cloud.

## SSH into the VMs
Update the SSH config file within `~/.ssh` to include the key, then connect to each VM using:

```bash
ssh vm1
ssh vm2
```

## Create a test topology
Use the `mininet_topology.py` script to set up 2 hosts.

## Create a VxLAN
On each VM, execute the following commands to set up VxLAN interfaces:

- For VM1:
    ```bash
    sudo ip link add vxlan0 type vxlan id 42 dev ens3 dstport 4789
    sudo ip addr add 10.0.0.1/24 dev vxlan0
    sudo ip link set up dev vxlan0
    ```

- For VM2:
    ```bash
    sudo ip link add vxlan0 type vxlan id 42 dev ens3 dstport 4789
    sudo ip addr add 10.0.0.2/24 dev vxlan0
    sudo ip link set up dev vxlan0
    ```

## Add Route to VxLAN from Mininet
Launch Mininet on each VM: `sudo python mininet_topology.py`

- For VM1: `h1 route add -net 10.0.0.0/24 gw 10.0.0.1` 
- For VM2: `h1 route add -net 10.0.0.0/24 gw 10.0.0.2` 

## Test the connection 
From within Mininet, test the connectivity:

- On VM1: `h1 ping 10.0.0.2`
- On VM2: `h1 ping 10.0.0.1`

If the pings are successful, connectivity has been established through the VxLAN.

