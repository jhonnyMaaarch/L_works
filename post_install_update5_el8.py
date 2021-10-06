#! /usr/bin/python3
####This will be the python module for OS install

"""
This script is modification on top of post_install_update5.py.
This script will work in RHEL 8.X, SLES 15, Ubuntu20 etc without any python workaround.

Original author : Sunny
Revised version : Alok
Date            : Nov 20, 2020
"""

import os, pdb
import subprocess
import shutil
from subprocess import getstatusoutput

host_name = ""

def main():
    # configure password
    password = input('Would you like to configure password (Y or N): ')
    if password == "Y":
        passwd = subprocess.check_output('passwd', shell=True)
    else:
        print("skipped setting root password.")

    # configure the hostname 
    command = "hostname"
    status,output = getstatusoutput(command)
    host_name = output
    print(f"Current hostname = {host_name}")

    confighostname = input('Would you like to configure hostname (Y or N): ')
    if confighostname == "Y":
        host_name = input("Enter hostname: ")
        command = f"hostnamectl set-hostname {host_name}"
        status,output = getstatusoutput(command)
        if status == 0:
            print(f"hostname {host_name} set successfully.")
        else:
            print(f"Unable to set hostname. Error = {status}")
    else:
        print("skipped setting hostname.")


    # configure network interface
    os.chdir('/etc/sysconfig/network-scripts')
#    os.system('ls')
    print("Current IP config = ")
    os.system('ip a s')
    
    num_int = input("How many interface would you like to configure(enter 0 to skip interface config): ") 
    num_interface = int(num_int)
    counter = 0
    
    for counter in range(num_interface):
       net_interface = input("Enter the interface to be configured (e.g "+" eno" + str(counter) + "): " ) 
       int_type = input("Is this the public interface (Y or N): ")
       if int_type == 'Y':
             pdb.set_trace()
             pub_hostname = subprocess.check_output('host ' + host_name + ".pok.stglabs.ibm.com", shell=True, encoding="utf-8")
             print(pub_hostname)
             pub_ip = input("Enter the IP indicated above: ")
             pub_net = "255.255.240.0"
             pub_bCast = "9.47.95.255"
             pubg_way = "9.47.95.254"
             os.system("ifconfig " + net_interface + " " + pub_ip + " netmask " + pub_net + " broadcast " + pub_bCast)
             os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')  
             p_ifcfg_file = ('ifcfg-'+net_interface)
             CreateFile = open(p_ifcfg_file, 'w+')
             CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + pub_ip + '\n' + 'NETMASK=' + pub_net + '\n' + 'GATEWAY=' + pubg_way + '\n' + 'DEFROUTE=yes')
             CreateFile.write("\n")
             CreateFile.close()
             os.system(f"cat {p_ifcfg_file}")
       elif int_type == 'N': 
             ip_list = []
             private_ip_finder = subprocess.check_output('hostname -i', shell=True, encoding="utf-8")
             my_str = str(private_ip_finder)
             ip_list = my_str.split()
             print(ip_list)
             for I in ip_list:
                right_IP = input('is '+ I + ' your IP: (Y or N) ' )
                if right_IP == "Y":
                    private_ip = I
                elif private_ip != I:
                    private_ip == '10.28.0.X'
                else:
                    os.system('IP not listed')

             private_net ='255.255.240.0'
             privateg_way ='10.28.0.1'
             os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')
             ifcfg_file = ('ifcfg-'+net_interface)
             CreateFile = open(ifcfg_file, 'w+')
             CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + private_ip + '\n' + 'NETMASK=' + private_net + '\n' + 'GATEWAY=' + privateg_way)
             CreateFile.write('\n')
             print(CreateFile.read())
             CreateFile.close()
    os.system('ls')
    os.system('ip a s') 

    # Configure routes
    print("Current route info = ")
    os.system('ip r s') 
    configroute = input('Would you like to configure route (Y or N): ')
    if configroute == 'Y':
        os.system('ip r del default via 10.28.0.30') 
        os.system('ip r a default via 9.47.95.254')
        print("New route info = \n")
        os.system('ip r s') 
    else:
        print("Skipped route updation")

#   configure repository
    print("Current repo list = ")
    os.system('yum repolist')    
    configrepo = input('Would you like to configure repo (Y or N): ')
    if configrepo == 'Y':
        os.system('host ftp3.linux.ibm.com')
        os.chdir('/root')
        os_arc = subprocess.check_output('uname -i', shell=True, encoding="utf-8")
        configureftp3 = input("Do you want to configure ftp3 repo (ftp3 credentials are required)(Y/N): ")
        if configureftp3 == 'Y':
            print("OS architecture is " + os_arc )
            os_arch = input("Enter the hardware architecture above (e.g ppc64): ")
            if os_arch == "ppc64" or os_arch == "ppc64le":
                os.system('scp -p c84f1u01:ibm-yum.sh ./')
                os.system('./ibm-yum.sh')
            elif os_arch == "x86_64":
                os.system('scp -p c84f1u01:ibm-rhsm.sh ./')
                os.system('./ibm-rhsm.sh')
            print("New repo list = \n")
            os.system('yum repolist')    
        else:
            print("ftp3 repo configuration skipped") 
    else:
        print("Skipped repo config")

    #   install packages
    print("Installing some basic packages...")
    os.system('yum -y install autofs')
    os.system('yum -y install xinetd')
    os.system('yum -y install kernel-devel')
    os.system('yum -y install gcc-c++')
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

    print("Post install configuration finished. Please check for any errors above and fix it manually.")

if __name__ == '__main__':
    main()
