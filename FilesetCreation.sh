#! /bin/bash

#cd /xiv
# create the sandbox directory to house your new vm cluster
#mkdir pkvm_sandbox2
#cd pkvm_sandbox2
#mkdir bigcluster

cd /xiv/kvm_sandbox2

# create fileset
mmcrfileset kvm_sandbox2 big-cluster --inode-space new
#Link the fileset
mmlinkfileset kvm_sandbox2 big-cluster -J /xiv/kvm_sandbox2/big-cluster
ls -ltr
cd big-cluster
# copy over relevant files into the sandbox2 dir
cp -p /xiv/kvm_Templates/rhel73.ppcle-template.raw ./

ls -ltr
cp -p /xiv/pkvm_Templates/deploy-cluster.sh ./
cp -p /xiv/pkvm_Templates/NSD_Deploy.py ./

./deploy-cluster.sh

# full path to install at /xiv/kvm_sandbox2/bigcluster
# path to vm template /xiv/kvm_sandbox2/bigcluster/rhel73.ppcle-template.raw
# cluster name sunny-cluster
# starting number for -vmX should always be 1
# amount of RAM per node 8192
# CPU per node 2
# bridge adapter br0
# All IPs are sequential y
# starting point 192.168.19.10
# gateway 192.168.180.247

mmclone show *
virsh list
# create 4 10GB disk
qemu-img create -f raw big-cluster-vm1-1.img 10G
qemu-img create -f raw big-cluster-vm1-2.img 10G
qemu-img create -f raw big-cluster-vm1-3.img 10G
qemu-img create -f raw big-cluster-vm1-4.img 10G
ls -ltr
du -sh
# attach the disk files to one VM
virsh attach-disk big-cluster-vm1 /xiv/kvm_sandbox2/bigcluster/big-cluster-vm1-1.img --target vdb --persistent --cache none --shareable
virsh attach-disk big-cluster-vm1 /xiv/kvm_sandbox2/bigcluster/big-cluster-vm1-3.img --target vdc --persistent --cache none --shareable
virsh attach-disk big-cluster-vm1 /xiv/kvm_sandbox2/bigcluster/big-cluster-vm1-3.img --target vdd --persistent --cache none --shareable
virsh attach-disk big-cluster-vm1 /xiv/kvm_sandbox2/bigcluster/big-cluster-vml-4.img --target vde --persistent --cache none --shareable

virsh shutdown VM
cd ..
# create snapshot
mmlsfileset kvm_sandbox2
mmcrsnapshot kvm_sandbox2 bigcluster:single-node-test
mmlssnapshot kvm_sandbox2

# To remove files
cd big-cluster

virsh shutdown vm
rm -rf *

cd ..
# To restore VMs
mmrestorefs kvm_sandbox2
mmlssnapshot kvm_sandbox2
mmrestorefs kvm_sandbox2 single-node-test -j big-cluster

df -h

#vi /var/adm/ras/*latest*
#
#mmtracectl --start # propagate the cluster config data all affected nodes
#
#To move the VM while online
virsh migrate --persistent --live mal_VMcluster-vm1 qemu+ssh://c20f2p8n02.gpfs.net/system
