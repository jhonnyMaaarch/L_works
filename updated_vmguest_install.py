#! /usr/bin/python
### VM creation and setup

import os
import subprocess
import shutil

def main():
    os.system('virsh list --all')
#from subprocess import getstatusoutputs
# Go into the vm directory
    vm_dir = raw_input("Enter a vm directory name e.g (/powerkvm): ")
    print('You entered %s'% vm_dir)
    try:
      os.mkdir(vm_dir)
    except OSError:
      print('directory already exist!')
      os.chdir(vm_dir)
    else:
      print('You have successfully created %s'% vm_dir)
      os.chdir(vm_dir)

    os.system('pwd')
    vm_name = raw_input('Enter the name of the domain e.g (c72f1c4p1v2): ')
    ram_size = raw_input('Enter memory size e.g (40960): ')
    Vcpus = raw_input('Enter number of CPU e.g (2, 4, etc): ')
    #Os_type = raw_input('Enter your os type (e.g linux): ')
    print('copy from the list of os variants provided below and provide it as your input.')
    subprocess.call('osinfo-query os', shell=True)
    os_variant = raw_input('Provide os variant from the list above e.g (rhl8.0): ')
    disk_block = raw_input('Provide the disk block to use for your installation e.g (/dev/sdb): ')
    xcat_server_ip = raw_input('Enter the IP of the xcat server e.g (192.168.180.24): ')
#    network_path = 'http://192.168.180.24:80/install/'
    install_dir = raw_input('Your network install directory e.g (192.168.180.24:80/install/ -  install): ')
    short_os = raw_input('Enter the OS to install e.g (rhel8.4): ')
    node_arch = raw_input('Enter OS architecture e.g (ppc64le): ')
    dom_ip = 'host '+vm_name
    vm_ip =subprocess.check_output(dom_ip, shell=True)
    print(vm_ip)
    host_ip = raw_input('Enter the IP displayed above: ')
    gateway_IP = raw_input('Enter your gateway IP e.g (192.168.180.247): ')
    Netmask = raw_input('Enter your netmask e.g (255.255.0.0): ')
    net_interface = raw_input('Enter your network interface e.g (enp0s1): ')

    subprocess.call('virt-install '+'--name '+vm_name+' --ram '+ram_size+' --vcpus '+Vcpus+' --os-type linux'+' --os-variant '+os_variant+' --disk '+disk_block+' --location '+'\'http://'+xcat_server_ip+':80/'+install_dir+'/'+short_os+'/'+node_arch+'\''+' --network bridge=br0 '+' --vnc '+' --extra-args '+'\"ip='+host_ip+'::'+gateway_IP+':'+Netmask+':'+vm_name+'.gpfs.net'+':none"',shell=True)
 
    # manage the .xml file generated from your virtual guest by moving it to the virtual directory.
    xml_file = subprocess.check_output('virsh dumpxml '+vm_name + ' | tee '+vm_name+'.xml', shell=True)
    try:
     shutil.copy(xml_file, vm_dir)
    except IOError:
     print('No such file or directory: %s'% vm_name)
    else:
     print('operation successful!')
    # confirm it has been moved
    os.getcwd()
    os.system('ls')
    
if __name__ == '__main__':
   main()
