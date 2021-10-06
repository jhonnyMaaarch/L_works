#! /usr/bin/python
####This will be the python module for update firmware - still working on it
import os
import subprocess
import shutil


def main():
    
    #Enter node to install
    host_name = raw_input("Enter hostname to install: ")
    subprocess.call('rpower %s' % host_name + ' stat', shell=True)
    
    if subprocess.call(host_name + ': on', shell=True):
       # Get the mac address
       subprocess.call('ping -c 1 %s' % host_name, shell=True)
       subprocess.call('arp -a %s' % host_name, shell=True)
       os.system('rinv ' + host_name + ' mac')
       print("Add the above mac address to the mac parameter")
       
       print("I am powering off " + host_name + " for install...")
       subprocess.call('rpower %s' % host_name + ' off', shell=True)
    else:
       print("Node already powered off, proceeding with install...")

    # Get the node mac address
    mac_addr = raw_input("Enter the mac address above here: ")
                              # subprocess.call('./chdef_mac.sh', shell=True)
                              # subprocess.Popen('chdef %s' % host_name + ' mac= %s' % mac_addr, shell=True)
    os.system('chdef ' + host_name + ' mac=' + mac_addr)
                              # os.system('chdef %s' % host_name + ' mac= %s' % mac_addr)
                               # subprocess.run('chdef %s' % host_name + ' mac= %s' % mac_addr, shell=True)
                               # subprocess.call('chdef %s' % host_name + ' mac= %s' % mac_addr, shell=True)
    # Provide the netboot parameter
    net_boot = raw_input("Enter netboot value (e.g xnba or pxe): ")
    os.system('chdef ' + host_name + ' netboot=' + net_boot)

    # makedhcp
    os.system('makedhcp ' + host_name)
    
    # Provide osimage
    os.system('lsdef -t osimage')
    os_image = raw_input("Enter osimage (e.g rhels8.0-x86_64-install-compute): ")
    os.system('nodeset ' + host_name + ' osimage=' + os_image)

    # provide target installation medium
    inst_source = raw_input("Enter source of install (e.g net: for network, hd: for Harddrive, CD: for CDROM): ")
    os.system('rsetboot ' + host_name + ' osimage=' + inst_source) 

    # One last check before power on
    subprocess.call('lsdef %s' % host_name, shell=True)
    
   # power on node
    os.system('rpower ' + host_name + ' on')
    os.system('rpower ' + host_name + ' on')
    os.system('tail -f /var/log/messages | grep -i ' + mac_addr)


if __name__ == '__main__':
   main()

