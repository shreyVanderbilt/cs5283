# !/bin/sh
#
# Shell script to stop a kubernetes cluster locally on our VM with just one
# machine serving as both a master and worker

# Before starting anything, we kill any existing K8s cluster
echo "reseting any existing K8s cluster and removing any files"
sudo kubeadm reset -f

echo "remove the ~/.kube etc files"
rm -fr ~/.kube
sudo rm -fr /etc/cni/net.d

