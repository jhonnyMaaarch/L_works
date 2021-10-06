#! /usr/bin/python3
import os
import subprocess
import shutil

def main():

    
    # install all the necessary virt rpm packages
    
    os.system('yum groupinstall "Virtualization Hypervisor"')
    os.system('yum groupinstall "Virtualization Client"')
    os.system('yum groupinstall "Virtualization Platform"')
    os.system('yum groupinstall "Virtualization Tools"')
    
    # start the virtualization service
    
    os.system('systemctl status libvirtd.service')
    
    virtServ_status = input('Would you like to start the libvirtd service: (Y or N): ')
    if virtServ_status == 'Y':
       os.system('systemctl start libvirtd.service')
    else:
       subprocess.call('echo continue', shell=True)
    

    os.system('systemctl status libvirtd.service')
    

    # configure network bridge
    vnet_cli = subprocess.check_output('virsh net-list --all', shell=True)
    print(vnet_cli)
    
    os.chdir('/etc/sysconfig/network-scripts')
    os.system('ls')
    
    os.system('ifconfig')
    # create the config file for the bridge interface
    or_int = input('Enter the primary network interface you want to bridge (e.g eno2): ') 
    or_conf = 'ifcfg-'+or_int
    os.system('cat '+ or_conf)
    ipAddr = input('Enter the IP address(e.g 10.20.28.1): ')
    br_int = input('Enter the bridge interface (e.g br0): ')
    br_conf = 'ifcfg-'+br_int
    CreateFile = open(br_conf, 'w+')
    CreateFile.writelines('###'+br_conf + '\n' + 'BRIDGING_OPTS=priority=28672'+ '\n' + 'TYPE=Bridge' + '\n' + 'BOOTPROTO=static' + '\n' + 'NAME=' + br_int + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR='+ipAddr + '\n' + 'NETMASK=255.255.0.0'+ '\n' + 'BROADCAST=192.168.255.255')
    CreateFile.write("\n")
    print(CreateFile.read())
    CreateFile.close()
    
    os.system('cp -p ' + or_conf + ' '+ or_conf + '_orig') 
    CreateFile = open(or_conf, 'w+')
    CreateFile.writelines('###'+or_conf + '\n' + 'DEVICE=' + or_int + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'BRIDGE=' + br_int)
    CreateFile.write("\n")
    print(CreateFile.read())
    CreateFile.close()

    os.system('brctl show')
    os.system('brctl addbr ' + br_int)
    os.system('ifconfig')
    os.system('brctl show')
    os.system('brctl addif ' + br_int + ' ' + or_int)
    os.system('ifconfig ' + br_int + ' ' + ipAddr + ' netmask 255.255.0.0 ' +'up')
    os.system('ifconfig ' + br_int + ' ' + 'up')
    os.system('ifconfig ' + or_int + ' ' + '0.0.0.0')
    os.system('virsh net-list --all') 
    os.system('brctl show')
    os.system('ifconfig')

  
    # configure the hostname
    host_name = input("Enter hostname: ")
    Node_name = subprocess.check_output('hostname %s' % host_name, shell=True)
    name_confirmation = subprocess.check_output('hostname '+ '-s', shell=True)
    print(name_confirmation)

    os.chdir('/etc/')
    os.system('ls')
    
    FileName = "hostname"
    CreateFile = open (FileName, 'w+')
    CreateFile.write(host_name + '.gpfs.net')
    CreateFile.write("\n")
    print(CreateFile.read())
    CreateFile.close()
   
    #install vnc
    os.system('yum install firefox* gnome*')
    os.system('yum install vnc*')
    os.system('vncserver -list')
    os.system('vncserver -geometry 1840x940')

    
    

if __name__ == '__main__':
    main()
