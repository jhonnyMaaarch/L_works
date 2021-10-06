#!/bin/bash
########################################################################
########################################################################
###                     author: Sunny Adeola                         ###
###                     email: osadeola@us.ibm.com                   ###
###                     date: 08-30-2019                             ###
### project: Module will require all parameters need for OS install  ###
### and perform the instalation afterwards                           ###
###                                                                  ###
########################################################################
########################################################################
read -p "Enter Virtual host name (e.g c71f1c1v1): " virtName
read -p "Enter memory size (e.g 8192): " memSize
read -p "Enter number of cpu (e.g 1) : " numCPU
read -p "Enter device to install at (e.g /dev/sdb): " deviceBL
read -p "Enter install file directory or location (e.g /powerkvm/) : " Loc
read -p "Enter OS to install (e.g RHEL-8.0.0-20190404.2-ppc64le-dvd1.iso): " OS_Name
osinfo-query os
read -p "Enter OS to install (e.g rhl8.0): " OS_ver
virt-install --name $virtName --memory $memSize --vcpus $numCPU --disk $deviceBL --cdrom $Loc/$OS_Name --os-variant $OS_ver --network bridge=br0

virsh dumpxml $virtName | tee $virtName.xml

mv $virtName.xml $Loc

echo "Your Virtual install is a success!"
