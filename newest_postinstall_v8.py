#! /usr/bin/python3
########################################################################
########################################################################
###                     author: Sunny Adeola                                    ###
###                     email: osadeola@us.ibm.com                              ###
### Project: RHEL post install. Mainly for OS version using pythonV3            ###
###          For OS versions using python v2 Please use the twin -              ###
###         newest_postinstall.py - found in /u/sunny/Tools or xcatmn3:         ###
########################################################################
########################################################################

import os
import subprocess
import shutil
from subprocess import getstatusoutput

def main():
   # Conigure dns
    os.chdir('/etc/')
    os.system('ls')
    try:
     shutil.copy('resolv.conf', 'resolv.conf_orig')
    except FileNotFoundError:
     print("File does not exist! Creating one")
     ask_to_createFile = input('Would you like to create one (Y/N): ')
     if ask_to_createFile == 'Y':
      Nameserver = '9.12.16.2'
      dnsFile = 'resolv.conf'
      CreateFile = open(dnsFile, 'w+')
      CreateFile.writelines('domain gpfs.net.' + '\n' + 'nameserver 192.168.180.253' + '\n' + 'nameserver fe80::42f2:e9ff:fe75:b40' + '\n' + 'nameserver fd55:faaf:e1ab:208:9:12:16:2' + '\n' + 'nameserver2 ' + Nameserver)
      CreateFile.write("\n")
      print(CreateFile.read())
      CreateFile.close()
     else:
      exit()
    else:
     os.system('ls') 
   
   # create a yum repository
    #os_dir = '/install/'
    #os_ver = input('Enter OS package to update (go to xcatmn3:/install/) to find what your os looks like e.g rhel8.4: ')
    #arch_cmd = 'uname -m'
    #stat, output = getstatusoutput(arch_cmd)
     
   # Nameserver = '9.12.16.2'
   # dnsFile = 'resolv.conf'
   # CreateFile = open(dnsFile, 'w+')
   # CreateFile.writelines('domain gpfs.net.' + '\n' + 'nameserver 192.168.180.253' + '\n' + 'nameserver fe80::42f2:e9ff:fe75:b40' + '\n' + 'nameserver fd55:faaf:e1ab:208:9:12:16:2' + '\n' + 'nameserver2 ' + Nameserver)    
   # CreateFile.write("\n")
   # print(CreateFile.read())
   # CreateFile.close()
    
    #   install packages
    os.system('yum -y install autofs')
    os.system('yum -y install xinetd')
    os.system('yum -y install kernel-devel')
    os.system('yum -y install gcc-c++')
    os.system('yum -y install ksh')
    os.system('yum -y install ksh')
    os.system('yum -y install gcc')
    os.system('yum -y install compat-libstdc++-33')
    os.system('yum -y install rsh')
    os.system('yum -y install make')
    os.system('yum -y install rsh-server')
    os.system('yum -y install lsscsi')
    os.system('yum -y install net-tools')
    os.system('yum -y install bind-utils')
    os.system('yum -y install device-mapper-multipath')
    os.system('yum -y install nfs-utils')
    os.system('yum -y install flex-devel')
    os.system('yum -y install git*')
    os.system('yum -y install nfs')

    os.system('scp xcatmn3:/u/admin/master_files/auto.master.linux /etc/auto.master')
    os.system('scp xcatmn3:/u/admin/master_files/auto.u.master /etc/auto.u')
    
    # start nfs service
    os.system('chkconfig --level 2345 nfs on')
    
    # start autofs service
    os.system('chkconfig --level 2345 autofs on')

    # systemctl start nfs-server.service

    os.system('systemctl start nfs.service')
    os.system('systemctl status nfs.service')
    
    os.system('systemctl start autofs.service')
    os.system('systemctl status autofs.service')

    os.system('ls /u/sunny')
    
    # initiate the xinetd activation process - xinetd is the daemon that starts ser
    # vices that provide internet services

    os.chdir('/u/sunny/scripts')
    shutil.copy('rsh-rh.tar', '/etc/xinetd.d')
    os.chdir('/etc/xinetd.d')
    os.system('tar xvf rsh-rh.tar')
    os.system('service xinetd stop')
    os.system('service xinetd start')

    os.system('/u/gpfstest/network/NTP/setupntp.linux')
    
    # configure network interface
    os.system('ifconfig')
    net_int = input('Enter the network interface to be configured; ')
    ipADDR= input('provide ip address (e.g 192.168.7.70): ')
    netMASK = '255.255.0.0'
    brdCAST = '192.168.255.255'
    os.chdir('/etc/sysconfig/network-scripts')
    shutil.copy('ifcfg-'+net_int, 'ifcfg-'+net_int+'_orig')
    netFile = 'ifcfg-'+net_int
    CreateFile = open(netFile, 'w+')
    CreateFile.writelines('###ifcfg-'+net_int + '\n' + 'DEVICE='+net_int + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + ipADDR + '\n' + 'NETMASK=' + netMASK + '\n' + 'BROADCAST=' + brdCAST)
    CreateFile.write('\n')
    CreateFile.read()
    CreateFile.close()
    
    subprocess.call('cat '+ netFile, shell=True) 
 


if __name__ == '__main__':
    main()
