#! /usr/bin/python3
import os
import subprocess
import shutil
from subprocess import getstatusoutput

def main():
    
    os.system('scp xcatmn3:net-tools-deprecated-2.0+git20180626.aebd88e-2.3.x86_64.rpm ./')
    os.system('rpm -ivh net-tools-deprecated-2.0+git20180626.aebd88e-2.3.x86_64.rpm ')
    
    os.system('zypper install iputils*')
    os.system('zypper install nfs*')
    os.system('zypper install vim*')
    os.system('zypper install wget')

    # create dns
    os.chdir('/etc/')
    os.getcwd()
    os.system('cp -p resolv.conf resolv.conf_orig')
    #stat, dns_filename = getstatusoutput(
    dns_filename = 'resolv.conf'
    os.system('cat resolv.conf')
    CreateFile = open(dns_filename, 'w+')
    CreateFile.writelines('domain gpfs.net' + '\n' + 'nameserver 192.168.180.253' + '\n' + 'search gpfs.net pok.stglabs.ibm.com ibm.com')
    CreateFile.write('\n')
    CreateFile.close()
    
    os.chdir('/etc/sysconfig/network')
    host_name = input('Enter the hostname to copy file from (e.g c42an1): ')
    os.system('ls')
    os.system('ifconfig')
    os.system('mv config config_orig')
    os.system('mv dhcp dhcp_orig')
    os.system('scp '+ host_name +':/u/sunny/sl15config ./config')
    os.system('scp '+ host_name +':/u/sunny/sl15dhcp ./dhcp')
    net_file = input('Enter the network file to configure (e.g ifcfg-eth0): ')
    os.system('cp -p ' + net_file +" "+ net_file + '_orig')
    priv_ip = 'hostname -i'
    stat, private_ip = getstatusoutput(priv_ip)
    CreateFile = open(net_file, 'w+')
    CreateFile.writelines('###ifcfg-'+net_file + '\n' + 'DEVICE='+net_file + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + private_ip + '\n' + 'NETMASK=' + '255.255.0.0' + '\n' + 'BROADCAST=' + '192.168.255.255')
    CreateFile.write("\n")
    CreateFile.close()
    os.system('ls')    


   # hostname file
    h_name = 'hostname -s'
    stat, host_Name = getstatusoutput(h_name)
    os.chdir('/etc/')
    host_name = 'hostname'
    CreateFile = open(host_name, 'w+')
    CreateFile.write(host_Name)
    CreateFile.close()

   # setup route to external resources
    os.system('route add -net default netmask 0.0.0.0 gw 192.168.180.247')
    os.system('route add -net ' + '9.0.0.0' + ' netmask ' + '255.0.0.0' + ' gw ' + 'xslesmn.gpfs.net')
    os.system('route add -net 195.0.0.0 netmask 255.0.0.0 gw 192.168.180.247')
 
    os.system('route')

    os.system('zypper addrepo https://download.opensuse.org/repositories/Kernel:/SLE15-SP2/standard/Kernel:SLE15-SP2.repo')
   
    os.system('zypper addrepo https://download.opensuse.org/update/openSUSE-stable/openSUSE:Leap:15.2:Update.repo')

    os.system('zypper addrepo https://download.opensuse.org/repositories/zypp:/SLE-15-SP2-Branch/openSUSE_Leap_15.2/zypp:SLE-15-SP2-Branch.repo')

    #download and install packages
    os.system('zypper in gcc gcc-32bit gcc43 gcc43-32bit gcc43-c++ gcc-c++ glibc-devel glibc-devel-32bit kernel-default-devel kernel-source libgomp43-32bit libstdc++43-devel libstdc++-devel linux-kernel-headers nfs-kernel-server lsscsi rsh-server autofs* net-tools*')

    #configure /u
    source_host = 'xcatmn1'
    os.system('scp '+ source_host +':/etc/auto.linux /etc/auto.linux')
    os.chdir('/etc')
    untar = 'tar xvf auto.linux'
    stat, untar_cmd = getstatusoutput(untar)
    os.system('chkconfig --set nfsserver on')
    os.system('chkconfig --set autofs on')
    os.system('service nfsserver stop')
    os.system('sleep 2')
    os.system('service nfsserver start')
    os.system('service autofs stop')
    os.system('sleep 2')
    os.system('service autofs start')
    os.system('ls /u/sunny')

    os.chdir('/etc/xinetd.d')
    os.system('tar xvf /u/sunny/scripts/rsh-suse.tar')
    os.system('service xinetd stop')
    os.system('service xinetd start')

    #set up NTP
    os.system('/u/gpfstest/network/NTP/setupntp.linux')

    os.system('ping -c 3 glogin03')
    
    os.system('zypper lr -u')

if __name__ == '__main__':
    main()   
   
