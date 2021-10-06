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
read -p "How many guests to install (e.g 1 ): " virtNunmber

while [ $virtNunmber -gt 0 ]
do
    read -p "Enter Virtual host name (e.g c71f1c1v1): " virtName
    read -p "Enter memory size (e.g 8192): " memSize
    read -p "Enter number of cpu (e.g 1) : " numCPU
    read -p "Enter device to install at (e.g /dev/sdb): " deviceBL
    read -p "Enter install file directory or location (e.g /powerkvm/) : " Loc
    read -p "Enter OS to install (e.g RHEL-8.0.0-20190404.2-ppc64le-dvd1.iso): " OS_Name
    read -p "Enter network interface to install at (e.g /dev/sdb): " Nic
    virt-install --name $virtName --memory $memSize --vcpus $numCPU --disk $deviceBL --cdrom $Loc/$OS_Name --network bridge=$Nic

    virsh dumpxml $virtName | tee $virtName.xml

    mv $virtName.xml $Loc
    ((virtNunmber--))
done

virsh list --all
echo "Your Virtual install is a success!"
