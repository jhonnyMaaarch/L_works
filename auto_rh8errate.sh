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

#copy dns configuration over from the dhcp server
scp 192.168.180.24:/etc/resolv.conf /etc/resolv.conf

#install all the enabling packages/rpms
yum -y install autofs xinetd kernel-devel gcc-c++ ksh gcc compat-libstdc++-33 rsh make rsh-server lsscsi net-tools bind-utils device-mapper-multipath nfs-utils flex-devel nfs*

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

host ftp3.linux.ibm.com

read -p "Enter first digit(s) in the IP address(es) above (e.g 9): " f_digit
read -p "Enter first disgit in netmask (e.g 255): " f_net
read -p "Enter gateway address (e.g 192.168.180.247): " g_way

route add -net "$f_digit".0.0.0 netmask "$f_net".0.0.0 gw $g_way

route 
#setup errata repository
#cd
#scp xcatmn3:ibm-rhsm.sh ./
#./ibm-rhsm.sh
cd /etc/yum.repos.d

read -p  "Enter OS version (e.g rh8):" os_ver

if [[ $os_ver == rh8 ]]; then
  scp xcatmn3:/u/sunny/Kernel_errata_rh8_1.repo ./
  yum repolist all
  yum update kernel*
else
  echo "os version Not specified!"
fi

cd /etc/yum.repos.d

echo "post install process is a SUCCESS!"

