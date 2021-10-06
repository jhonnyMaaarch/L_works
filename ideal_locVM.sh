#!/bin/bash
#post install after pkvm installation
#cd /
#mkdir /powerkvm
read -p "Enter desired directory name: (e.g powerkvm) " dirName
mkdir /$dirName
if [ "File exists" ]
    then
        echo "Directory exist! I am going in!"
        cd /$dirName
    else
        cd /$dirName
    fi

#cd /powerkvm
cd /$dirName
#copy OS into the appr directory
#scp prh03:/iso/ubuntu-16.04.3-server-ppc64el.iso ./
#scp c72f1c3p1:/powerkvm/RHEL-7.4-20170711.0-Server-ppc64le-dvd1.iso ./
# echo -p "would you like to copy over any file: "
# scp c72f1c4p1:/powerkvm/RHEL-7.3-20161019.0-Server-ppc64le-dvd1.iso ./
echo "Please make sure your iso image is already copied over."
read -p "Enter the domain name: " domName
read -p "Enter RAM size:(e.g 40960) " ramSize
read -p "Enter the partition to install in:(e.g /dev/sdb) " domPartition
read -p "Enter OSimage location: (e.g /powerkvm) " osLocation
read -p "Enter the os image to be ran: " osImage
#echo -p "Enter the domain name: " domName
#install os
virt-install --name $domName --ram $ramSize --disk $domPartition --cdrom /$osLocation/$osImage --nonetwork

#virt-install --name $domName --ram $ramSize --disk $domPartition --cdrom /powerkvm/RHEL-7.3-20161019.0-Server-ppc64le-dvd1.iso --nonetwork

#post install
#virsh shutdown test
virsh shutdown $domName

read -p "Enter the xml file: (e.g c72f1c8p1v1.xml) " xmlFile
#virsh dumpxml test | tee c72f1c8p1v1.xml
virsh dumpxml $domName | tee $xmlFile

#virsh undefine test

virsh undefine $domName

#virsh define c72f1c8p1v1.xml

virsh define $xmlFile

#vi c72f1c8p1v1.xml
vi $xmlFile

#virsh edit c72f1c8p1v1
