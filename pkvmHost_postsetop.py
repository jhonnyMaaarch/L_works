#! /usr/bin/python

import sys
import os
import shutil

def main()

    #configure route
    old_new = raw_input('is this configuration on old (192) network (Y or N): ')
    if old_new == "Y"
        g_way = '192.168.180.247'
        n_mask = '255.0.0.0'
        d_ip = '9.0.0.0'
    else:
        if old_new == "N"
        dest_ip = raw_input("Enter destination IP (e.g 9.0.0.0): ")
        net_mask = raw_input("Enter netmask (e.g 255.0.0.0): ") 
        gate_way = raw_input("Enter Gateway IP (e.g 192.168.180.247): ")
        d_ip = str(dest_ip)
        n_mask = str(net_mask)
        g_way = str(gate_way)


    route_conf = subprocess.check_output('route add -net ' + d_ip + ' ' + n_mask + ' ' + g_way, shell=True )

    os.system('route')
    
    # install packages
    os.system('yum -y install autofs')
    os.system('yum -y install xinetd')
    os.system('yum -y install kernel-devel')
    os.system('yum -y install gcc-c++')
    os.system('yum -y install ksh')
    os.system('yum -y install gcc')
    os.system('yum -y install make')
    os.system('yum -y install bind-utils')
    os.system('yum -y install device-mapper-multipath')
    os.system('yum -y install git*')
    os.system('yum -y install nfs')

    # configure bridge interface
    os.system('ifconfig')
    os.system('brctl')
    
    os.chdir('/etc/sysconfig/network-scripts')
    cur_dir = subprocess.check_out('pwd', shell=True)
    print("You are currently in this directory: " + cur_dir)
    os.system('ls')

    # configure your bridge interface
    br_int = raw_input('Enter the bridge interface (e.g br0): ')
    net_mask = raw_input('Enter the network netmask (e.g 255.255.0.0): ')
    private_ip = subprocess.check_output('hostname -i', shell=True)
    bri_intFile = ('ifcfg'+br_int)
    
    CreateFile = open(bri_intFile, 'w+')
    CreateFile.writelines('###ifcfg-'+br_int + '\n' + 'DEVICE='+br_int + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'TYPE=Bridge' + '\n'+ 'IPADDR=' + private_ip + '\n' + 'NETMASK=' + pub_net + '\n' + 'GATEWAY=' + g_way +  '\n' + 'NM_CONTROLLED=no')
    
    ori_int = raw_input('Enter the original interface (e.g eth0): ')
    ori_intFile = ('ifcfg'+ori_int)
    CreateFile = open(ori_intFile, 'w+')
    CreateFile.writelines('###ifcfg-'+ori_int + '\n' + 'DEVICE='+ori_int + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'BRIDGE=' + br_int +  '\n' + 'NM_CONTROLLED=no')
    
    os.system('brctl addbr ' + 
   
    
      
if __name__ == '__main__':
   main()

    


