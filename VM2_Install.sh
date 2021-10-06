#!/bin/bash
########################################################################
########################################################################
###                     author: Sunny Adeola                         ###
###                     email: osadeola@us.ibm.com                   ###
###                     date: 09-09-2019                             ###
### project: Module will require all parameters need for OS install  ###
### and perform the instalation afterwards                           ###
###                                                                  ###
########################################################################
########################################################################
virsh list --all

read -p "Enter Virtual host name (e.g c71f1c1v1): " virtName
read -p "Enter memory size (e.g 40960): " memSize
read -p "Enter number of cpu (e.g 1) : " numCPU
read -p "Enter device to install at (e.g /dev/sdb): " deviceBL
#read -p "Enter network install directory or location (e.g 'http://192.168.180.242:80/install/rhels8.0le/ppc64le' ) : " Loc

host $virtName 

read -p "Enter IP address (e.g 192.168.117.222): " $ipAddr
read -p "Enter network interface (e.g enp0s1): " netInterface
osinfo-query os
read -p "Enter OS to install (e.g rhel7): " OS_ver
#virt-install --name $virtName --memory $memSize --vcpus $numCPU --disk $deviceB#L --location $Loc --os-variant $OS_ver --network bridge=br0 --extra-args " ip=$#ipAddr::192.168.180.247:255.255.0.0:$virtName.gpfs.net:$netInterface:none"

virt-install --name $virtName --memory $memSize --vcpus $numCPU --disk $deviceBL --location 'http://192.168.180.242:80/install/rhels8.0le/ppc64le' --os-variant OS_ver --network bridge=br0 --extra-args "ip=$ipAddr::192.168.180.247:255.255.0.0:$virtName.gpfs.net:$netInterface:none"

virsh dumpxml $virtName | tee $virtName.xml

read -p "Enter location to copy .xml file to (e.g /powerkvm): " FileLoc
mv $virtName.xml $FileLoc

echo "Your Virtual install is a success!"
