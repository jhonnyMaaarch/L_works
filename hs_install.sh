#!/bin/bash
######################################################
####Module will define node objects and parameters####
# Developed by: Sunny Adeola                      ####
# Date:         05/01/2020                        ####
# Contact:      osadeola@us.ibm.com               ####
######################################################
# Get node name
read -p "Enter Node name (e.g hs22n71): " Node_name
rinv $Node_name mac

read -p "Enter appropriate mac address: " mac_addr

chdef $Node_name mac=$mac_addr
chdef $Node_name installnic=mac
chdef $Node_name primarynic=mac

read -p "Enter netboot option (e.g pxe, xnba, grub2: " netboot_opt
chdef $Node_name netboot=$netboot_opt

rpower $Node_name stat
if rpower $Node_name stat = "on"
then
    rpower $Node_name off
fi
if rpower $Node_name stat = "off"
then
    echo "$Node_name is ready to be provisioned"
fi

makedhcp $Node_name
lsdef -t osimage

read -p "Enter OS image: " os_image
nodeset $Node_name osimage=$os_image

rbootseq $Node_name net,hd0,cdrom

lsdef $Node_name

echo "are you ready to power on node:(y OR n)"
read poweroN
    if [ "$poweroN" = "n" ]
    then
        lsdef $Node_name
    fi

    if [ "$poweroN" = "y" ]
    then
    rpower $Node_name on
    fi

# track progess through network install
tail -f /var/log/messages | grep -i $mac_addr
