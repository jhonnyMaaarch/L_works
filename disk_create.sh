#! /bin/bash

############################################################################
# - Before starting this module, make sure you are logged into:
# c20f2p8n05 and are inside /xiv/kvm_sandbox2 
# - This module will create a VM directory that you provide to it
#    inside /xiv/kvm_sandbox2
# -It will copy over relevant files from the /xiv/kvm_Templates
# - create the vm
# - create disks and attach the disks to the VM(s)
#          Author: Sunny Adeola
#           email: osadeola@us.ibm.com
#     




#ACCCESS THE SANDBOX DIRECTORY TO CREATE A VM DIRECTORY
cd /xiv/kvm_sandbox2

echo "make a VM directory to store your vm files: "
read vmFile

mkdir $vmFile

cd $vmFile

#read -p "How many template files do you want to copy from template directory: " Num_copy

#while [ $Num_copy -gt 0 ]
#do
#    read -p "Enter the template file  to copy: " Templ_file
#    cp -p /xiv/kvm_Templates/$Templ_file ./
#    ((Num_copy--))
#done 

# RUN THE DEPLOY CLUSTER SCRIPTS
#./deploy-cluster.sh

# Create desirable number of disks based on number of Virtual machines
virsh list --all

read -p "Enter your number of VM (e.g 1): " num_VM

read -p "Enter the size of disk (e.g 30G): " Disk_size

while [ $num_VM -gt 0 ]
do
    read -p "Enter you vmname here (e.g test-vm1): " VM_Name
    qemu-img create -f raw $VM_Name.img $Disk_size
    ((num_VM--))
done

ls -ltr
du -sh
# Attach the disks created above with the vm

read -p "Enter number of disks created:" Num_OfDisk

while [ $Num_OfDisk -gt 0 ]
do
   read -p "Enter your vm to attach disk to (e.g test-vm1): " VM_Name
   read -p "Enter your .img to attach disk to(e.g test-vm1.img): " VM_image
   read -p "Enter partition (e.g vdb): " partition
   virsh attach-disk $VM_Name /xiv/kvm_sandbox2/$vmFile/$VM_image --target $partition --persistent --cache none --shareable
   ((Num_OfDisk--))
done

virsh list --all
echo "Your Virtual disk creation process is a success!"

