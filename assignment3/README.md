Online team 4
- Shreyank Patel
- Justin Summer
- Nelson Torres


Intially we setup VxLan0 on our 2 Chamelon VMS

IP ADDRESS FOR VM1: 192.168.5.162
IP ADDRESS FOR VM2: 192.168.5.251


We ran the following commands on VM1
```bash
sudo ip link delete dev vxlan0
sudo ufw disable
sudo ip link add vxlan0 type vxlan id 100 local 172.31.1.107 remote 172.31.13.110 dev eth0 dstport 4789
sudo ip addr add 192.168.100.1/24 dev vxlan0
sudo ip link set vxlan0 up
sudo ip route add 10.0.2.0/24 via 192.168.100.2 dev vxlan0
```

Similarly we ran the following commands on VM2
```bash
sudo ip link delete dev vxlan0
sudo ufw disable
sudo ip link add vxlan0 type vxlan id 100 local 172.31.13.110 remote 172.31.1.107 dev eth0 dstport 4789
sudo ip addr add 192.168.100.2/24 dev vxlan0
sudo ip link set vxlan0 up
sudo ip route add 10.0.1.0/24 via 192.168.100.1 dev vxlan0
```

Next we starting setting up UERANSIM on VM1 by running the following commands
```bash
git clone https://github.com/aligungr/UERANSIM
sudo apt update && sudo apt upgrade
sudo apt install make
sudo apt install gcc
sudo apt install g++
sudo apt install libsctp-dev lksctp-tools
sudo apt install iproute2
sudo snap install cmake --classic
cd UERANSIM
make 
```

Next we made the necessary changes to the config yaml files and then ran 
```bash
sudo ./nr-gnb -c ../config/custom-open5gs-gnb.yaml
```

![image](https://raw.githubusercontent.com/shreyVanderbilt/cs5283/main/assignment3/snapshots/MS1_UERANSIM_1.png)

Below are the logs from VM2
![image](https://raw.githubusercontent.com/shreyVanderbilt/cs5283/main/assignment3/snapshots/MS1_UERANSIM_LOG_1.png)


Then we started working on getting Open5gs setup on VM2 by running the following commands
```bash
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt update
sudo apt install -y mongodb-org
sudo systemctl start mongod
sudo systemctl status mongod.service
sudo systemctl enable mongod
#Open5gs
sudo add-apt-repository ppa:open5gs/latest
sudo apt update
sudo apt install open5gs
#WebUI
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt update
sudo apt install nodejs -y
curl -fsSL https://open5gs.org/open5gs/assets/webui/install | sudo -E bash -
```

Unfortunately, there were issues running the latest version of open5gs (v2.7.0) so we have to remove and reinstall open5gs v2.6.6.

However before we could finish re-installing open5gs v 2.6.6 Chameloen cloud started to experience outages. 

So we decided to create 2 EC2 instances on AWS under the same subnet and VPC and try to complete the programming assginment there.

We re did all the previously mentioned steps on the 2 EC2 instance and were able to get Open5gs v2.6.6 running.

Except we had to run different commands to get open5gs v2.6.6 setup. We ran the following commands
```bash
#Open5gs Setup
git clone -branch v2.6.6 https://github.com/open5gs/open5gs
cd open5gs
meson build --prefix=`pwd`/install
ninja -C build
cd build
ninja install
cd ../
./install/bin/open5gs-nrfd &
./install/bin/open5gs-scpd &
./install/bin/open5gs-amfd &
./install/bin/open5gs-smfd &
./install/bin/open5gs-upfd &
./install/bin/open5gs-ausfd &
./install/bin/open5gs-udmd &
./install/bin/open5gs-pcfd &
./install/bin/open5gs-nssfd &
./install/bin/open5gs-bsfd &
./install/bin/open5gs-udrd &
./install/bin/open5gs-mmed &
./install/bin/open5gs-sgwcd &
./install/bin/open5gs-sgwud &
./install/bin/open5gs-hssd &
./install/bin/open5gs-pcrfd &

#WebUI Setup
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list

sudo apt update
sudo apt install nodejs -y

cd webui
npm ci

ssh -i "vm_computer_network.pem" ubuntu@ec2-3-92-18-149.compute-1.amazonaws.com
```


Below is an imaage of the WebUI for Open5gs we were able to get running. 
![image](https://raw.githubusercontent.com/shreyVanderbilt/cs5283/main/assignment3/snapshots/Open5gs_WebUI.png)

However we were not able to setup the VxLan connections on the 2 ECS instance. We ran the following code to get the Vxlan0 setup 
IP ADDRESS FOR VM1: 172.31.1.107
IP ADDRESS FOR VM2: 172.31.13.110

# Helper commands
```bash
sudo ip link delete dev vxlan0 # if you need to delete the VxLAN
sudo ufw disable # to help clean up the iptables
# From VM1 enter the following commands:
sudo ip link add vxlan0 type vxlan id 100 local 172.31.1.107 remote 172.31.13.110 dev ens3 dstport 4789
sudo ip addr add 192.168.100.1/24 dev vxlan0
sudo ip link set vxlan0 up
sudo ip route add 10.0.2.0/24 via 192.168.100.2 dev vxlan0

#From VM2 enter the following commands:
sudo ip link add vxlan0 type vxlan id 100 local 172.31.13.110 remote 172.31.1.107 dev ens3 dstport 4789
sudo ip addr add 192.168.100.2/24 dev vxlan0
sudo ip link set vxlan0 up
sudo ip route add 10.0.1.0/24 via 192.168.100.1 dev vxlan0
```

EC2_VM1:
![image](https://github.com/shreyVanderbilt/cs5283/blob/main/assignment3/snapshots/EC2_VM1_NETWORK_SETTING.png)

EC2_VM2: 
![image](https://github.com/shreyVanderbilt/cs5283/blob/main/assignment3/snapshots/EC2_VM2_NETWORK_SETTING.png)




