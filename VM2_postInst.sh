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

#copy dns configuration over from the dhcp server
#read -p "Enter the host to copy repos from (e.g c7f1c3p1): " hostrepos
#ping -c 3 $hostrepos
scp 192.168.180.24:/etc/resolv.conf /etc/resolv.conf
read -p "Enter the host to copy repos from (e.g c7f1c3p1): " hostrepos
ping -c 3 $hostrepos
scp $hostrepos:/etc/yum.repos.d/local-repository-0.repo /etc/yum.repos.d
#install all the enabling packages/rpms
yum -y install autofs
yum -y install nfs*

#copy over auto.master file - the automount master file for specifying directori# es to be controlled along with their corresponding map files.
scp xcatmn3:/u/admin/master_files/auto.master.linux /etc/auto.master

# copy over the auto.u - the actual u file with users directories 
scp xcatmn3:/u/admin/master_files/auto.u.master /etc/auto.u

# start nfs service
chkconfig --level 2345 nfs on

# start autofs service
chkconfig --level 2345 autofs on

# systemctl start nfs-server.service

systemctl start nfs.service

systemctl start autofs.service


# initiate the xinetd activation process - xinetd is the daemon that starts ser
# vices that provide internet services

cd /u/sunny/scripts
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

ls /u/sunny
