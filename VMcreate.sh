#!/bin/bash
########################################################################
########################################################################
###                     author: Sunny Adeola                            ###
###                     email: osadeola@us.ibm.com                      ###
###                     date: 09-14-2019                                ###
###Ensure that the local install scripts and or the network install     ###
###scripts are in the same directory as this script before running it   ###
###                                                                     ###
########################################################################
########################################################################

virsh list --all
echo "Is this a network install (y or n): "
read installType
    if [ "$installType" = "y" ]
    then
    ls -lha
    read -p "Enter the network install script (e.g VM3_install.sh) :" net_Install
    chmod +x $net_Install
    ./$net_Install
    fi
    
    if [ "$installType" = "n" ]
    then
    echo "You must be installing from a local directory!"
    ls -lha
    read -p "Enter the local install script (e.g VM_install.sh) :" local_Install
    chmod +x $local_Install
    ./$local_Install
    fi

