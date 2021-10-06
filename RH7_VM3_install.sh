#!/bin/bash
########################################################################
########################################################################
###                     author: Sunny Adeola                         ###
###                     email: osadeola@us.ibm.com                   ###
###                     date: 01-9-2020                              ###
### project: Module will require all parameters need for OS install  ###
### and perform the instalation afterwards                           ###
###Latest upgrade for RH 7.2                                         ###
########################################################################
########################################################################
virsh list --all

read -p "Enter Virtual host name (e.g c71f1c1v1): " virtName
read -p "Enter memory size (e.g 40960): " memSize
read -p "Enter number of cpu (e.g 1) : " numCPU
read -p "Enter device to install at (e.g /dev/sdb): " deviceBL

host $virtName

read -p "Enter IP address (e.g 192.168.117.222): " ipAddr
osinfo-query os
read -p "Enter OS to install (e.g rhel7): " OS_ver

read -p "Enter network interface (e.g enp0s1): " netInterface
virt-install --name $virtName --memory $memSize --vcpus $numCPU --disk $deviceBL --location 'http://192.168.180.242:80/install/rhels7.2/ppc64' --os-variant $OS_ver --network bridge=br0 --extra-args "ip=$ipAddr::192.168.180.247:255.255.0.0:$virtName.gpfs.net:$netInterface:none"

virsh dumpxml $virtName | tee $virtName.xml

read -p "Enter install file directory to place .xml file (e.g /powerkvm/) : " Loc
mv $virtName.xml $Loc

virsh list --all

echo "Your Virtual install is a success!"
