# !/bin/sh
#
# Shell script to restart a kubernetes cluster locally on our VM with just one
# machine serving as both a master and worker

# Before starting anything, we kill any existing K8s cluster
echo "reseting any existing K8s cluster and removing any files"
sudo kubeadm reset -f
echo "remove the ~/.kube etc files"
rm -fr ~/.kube
sudo rm -fr /etc/cni/net.d

# make sure swap is turned off
echo "turning swap off"
sudo swapoff -a

# restart containerd and maybe docker to get the K8s to really work.
echo "Restarting containerd and docker"
sudo systemctl restart containerd.service
sudo systemctl restart docker.service