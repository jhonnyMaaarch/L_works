#!/bin/bash
########################################################################
########################################################################
###                     author: Sunny Adeola                         ###
###                     email: osadeola@us.ibm.com                   ###
###                     date:01-07-2019                              ###
### project: Module will perform post installation for redhat nodes  ###
###                                                                  ###
###                                                                  ###
########################################################################
########################################################################
passwd

# configure Repository
cd /etc/yum.repos.d
echo "Enter between RH8 or RH8.1"
read -p "Enter the OS repos to copy over (e.g RH8 or RH8.1): " OS_repo

if ["$OS_repo" = "RH8"]
then
    cd /etc/yum.repos.d/
    scp xcatmn3:/u/sunny/RH8.0_repos ./
fi
if ["$OS_repo" = "RH8.1"]
then
    cd /etc/yum.repos.d/
    scp xcatmn3:/u/sunny/RH8.1_repos ./
fi


 
#/etc/yum.repos.d/local-repository-0.repo
#copy dns configuration over from the dhcp server
scp 192.168.180.24:/etc/resolv.conf /etc/resolv.conf

#install all the enabling packages/rpms
yum -y install autofs 
yum -y install xinetd 
yum -y install kernel-devel 
yum -y install gcc-c++ 
yum -y install ksh 
yum -y install make 
yum -y install bind-utils 
yum -y install device-mapper-multipath 
yum -y install nfs*


#copy over auto.master file - the automount master file for specifying directori# es to be controlled along with their corresponding map files.
scp xcatmn3:/u/admin/master_files/auto.master.linux /etc/auto.master

# copy over the auto.u - the actual u file with users directories 
scp xcatmn3:/u/admin/master_files/auto.u.master /etc/auto.u


systemctl start nfs.service

systemctl start autofs.service

ls /u/shujun

# initiate the xinetd activation process - xinetd is the daemon that starts ser
# vices that provide internet services

cd /u/shujun/scripts
cp rsh-rh.tar /etc/xinetd.d
cd /etc/xinetd.d
tar xvf rsh-rh.tar
service xinetd stop
service xinetd start

# scp xcatmn1:/u/admin/master_files/auto.u.master /etc/auto.u
/u/gpfstest/network/NTP/setupntp.linux

# configure static interface
echo "Enter you NIC interface here: "
read Nic_int
/u/sunny/szinterface $Nic_int
# Activate syslog

mv -f  /etc/rsyslog.conf /etc/rsyslog.conf.orig
mv -f  /etc/rsyslog.conf.XCATORIG /etc/rsyslog.conf
service rsyslog stop
service rsyslog start
ls -l /var/log/messages
