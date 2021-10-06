#! /usr/bin/python
# To set up bridge interface
import os
import subprocess
import shutil


def main():
    
    # configure password
    password = raw_input('Would you like to configure password (Y or N): ')
    if password == "Y":
        passwd = subprocess.check_output('passwd', shell=True)
    else:
        os.system('echo proceeding...')

    # configure the hostname
    host_name = raw_input("Enter hostname: ")
    Node_name = subprocess.check_output('hostname %s' % host_name, shell=True)
    name_confirmation = subprocess.check_output('hostname '+ '-s', shell=True)
    print(name_confirmation)

    root_dir = os.getcwd()
    print("current directory is: "+ root_dir)
    subprocess.call('ls')

    os.chdir('/etc/')
    os.system('ls')

    FileName = "hostname"
    CreateFile = open (FileName, 'w+')
    CreateFile.write(host_name)
    CreateFile.write("\n")
    print(CreateFile.read())
    CreateFile.close()

    os.system('cat /etc/hostname')

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

#   configure public ip
    pub_conf = raw_input('Would you like to configure public IP. This will aid with vnc setup (y/n): ')
    if pub_conf == 'y':
     os.chdir('/etc/sysconfig/network-scripts')
     os.system('ifconfig')
     net_interface = raw_input('Enter your public network interface (e.g eno3): ')
     pub_hostname = subprocess.check_output('host ' + host_name + ".pok.stglabs.ibm.com", shell=True)
     print(pub_hostname)
     pub_ip = raw_input("Enter the IP indicated above: ")
     pub_net = "255.255.240.0"
     pub_bCast = "9.47.95.255"
     pubg_way = "9.47.95.254"
     os.system("ifconfig " + net_interface + " " + pub_ip + " netmask " + pub_net + " broadcast " + pub_bCast)
     os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')
     p_ifcfg_file = ('ifcfg-'+net_interface)
     CreateFile = open(p_ifcfg_file, 'w+')
     CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + pub_ip + '\n' + 'NETMASK=' + pub_net + '\n' + 'GATEWAY=' + pubg_way)
     CreateFile.write("\n")
     print(CreateFile.read())
     CreateFile.close()
    else:
     os.system('echo proceeding...')

     

#   configure repository
    os.system('host ftp3.linux.ibm.com')
    os.system('route add -net ' + 'default' + ' netmask ' + '0.0.0.0' + ' gw ' + '9.47.95.254')
    subprocess.call('route del -net default netmask 0.0.0.0 gw '+'10.28.0.30', shell=True)
    os.system('route')
    os.chdir('/root')
    os_arc = subprocess.check_output('uname -i', shell=True)
    print("OS architecture is " + os_arc )
    os_arch = raw_input("Enter the hardware architecture above (e.g ppc64): ")
    if os_arch == "ppc64":
       os.system('scp -p c84f1u01:ibm-yum.sh ./')
       os.system('./ibm-yum.sh')
    elif os_arch == "ppc64le":
       os.system('scp -p c84f1u01:ibm-yum.sh ./')
       os.system('./ibm-yum.sh')
    elif os_arch == "x86_64":
       os.system('scp -p c84f1u01:ibm-rhsm.sh ./')
       os.system('./ibm-rhsm.sh')
    else:
        os.system('No defined repository')

    print("current directory is: "+ root_dir)
    os.chdir('/etc/yum.repos.d/')
    os.system('ls')
    os.chdir('/root')

#   NetworkManager

    os.system('systemctl status NetworkManager')
    # if above show not active
    power_stat = raw_input('Would you like to start this NetworkManager service (y/n): ')
    if power_stat == 'y':
       os.system('systemctl start NetworkManager')
       subprocess.call('sleep '+'10', shell=True)
       os.system('systemctl enable NetworkManager')
       os.system('systemctl status NetworkManager')
    elif power_stat == 'n':
       os.system('echo proceeding...')
    else:
       os.system('echo lower case (y/n) required')
    
    # configure bridge interface
    os.system('nmcli con show')
    os.system('nmcli con show --active')
    bridge_name = raw_input('provide the bridge interface name (e.g br0): ')
    bridge_int = 'bridge-'+bridge_name
    subprocess.call('sudo nmcli con add ifname '+ bridge_name + ' type bridge con-name '+ bridge_name, shell=True)
    os.system('nmcli con show --active')
    os.system('ifconfig')
    
    # now add the slave to the master bridge
    or_interface = raw_input('provide the original network interface (e.g enP3p9s0f0): ')
    subprocess.call('sudo nmcli con add type bridge-slave ifname '+ or_interface + ' master '+ bridge_name, shell=True)
    subprocess.call('nmcli con show', shell=True)
    os.system('nmcli con show --active')

    #disable spanning Tree
    subprocess.call('sudo nmcli con modify '+bridge_name+ ' bridge.stp no', shell=True)
    os.system('nmcli con show --active')
    subprocess.call('nmcli -f bridge con show '+ bridge_name, shell=True)
    
    # configure the network address and mask on the bridge interface
    print('Your mask in this case is '+ '10.28.0.36/20'+ ' just enter y when you see it displayed.')
    find_mask = subprocess.check_output('ip addr | grep '+or_interface, shell=True)
    for I in find_mask.split():
        ip_mask = raw_input('is '+I+' your mask (y/n): ')
        if ip_mask == 'y':
           subprocess.call('sudo nmcli connection modify '+bridge_name+' ipv4.addresses '+''+'"'+I+'"'+'', shell=True)
           subprocess.call('nmcli -f bridge con show '+ bridge_name, shell=True)        
           break
        else:
           continue
   # print('I am suggesting the following gateway routes based on my command. The gateway may not be on the list. ')
    ip_gateway = subprocess.check_output('ip route', shell=True)
    print('gateway in this case is ' + '10.28.0.1')
   # for ip in ip_gateway.split():
   #     ip_gw = raw_input('is '+ip+' your gateway (y/n): ')
   #     if ip_gw == 'y':
   #        subprocess.call('sudo nmcli connection modify '+bridge_name+' ipv4.gateway '+''+'"'+ip+'"'+'', shell=True)
   #     else:
   #        continue
    ip_gw = '10.28.0.1'
    subprocess.call('sudo nmcli connection modify '+bridge_name+' ipv4.gateway '+''+'"'+ip_gw+'"'+'', shell=True)
    subprocess.call('cat /etc/resolv.conf',shell=True)
    dns_addr = raw_input('copy the dns address from above (if correct) and paste here: ')
    subprocess.call('sudo nmcli connection modify '+bridge_name+' ipv4.dns '+''+'"'+dns_addr+'"'+'', shell=True)
    dns_search = raw_input('copy the dns search domain from above (if correct) and paste here: ')
    subprocess.call('sudo nmcli connection modify '+bridge_name+' ipv4.dns-search '+''+'"'+dns_search+'"'+'', shell=True)
    ipv4_method = raw_input('Enter ipv4 method (auto/manual): ')
    subprocess.call('sudo nmcli con modify '+bridge_name+' ipv4.method '+''+'"'+ipv4_method+'"'+'', shell=True)
    subprocess.call('sudo nmcli con up '+ bridge_name, shell=True)
    subprocess.call('sudo nmcli d set ifname '+bridge_name+' autoconnect yes', shell=True)
    subprocess.call('nmcli con show', shell=True)
    #wait_time = int(10)
    subprocess.call('sleep '+'10', shell=True)
    # Verify network setting
    subprocess.call('ip a s', shell=True)
    subprocess.call('ip a s '+ bridge_name, shell=True)
    
    del_or = raw_input('Would you now like to delete the original interface? This is necessary to fully activete the bridge (y/n): ')
    if del_or == 'y':
       subprocess.call('sudo nmcli connection delete '+or_interface, shell=True)
    else:
      os.system('echo proceeding...')
   
    os.system('nmcli con show')
    os.system('nmcli con show --active')
    subprocess.call('ip a show '+bridge_name, shell=True)
    subprocess.call('nmcli device', shell=True)
    subprocess.call('ip link show master '+bridge_name, shell=True)
    subprocess.call('bridge link show', shell=True)
    subprocess.call('bridge link show dev'+or_interface, shell=True)
    
    subprocess.call('sleep '+'10', shell=True)
    # Now you may install all the necessary packages
    os.system('yum groupinstall "Virtualization Hypervisor"')
    os.system('yum groupinstall "Virtualization Client"')
    os.system('yum groupinstall "Virtualization Platform"')
    os.system('yum groupinstall "Virtualization Tools"')

    # start the virtualization service

    os.system('systemctl status libvirtd.service')
    
    virtServ_status = raw_input('Would you like to start the libvirtd service: (Y or N): ')
    if virtServ_status == 'Y':
       os.system('systemctl start libvirtd.service')
    else:
       subprocess.call('echo continue', shell=True)


    os.system('systemctl status libvirtd.service')

    
    # configure network bridge
    vnet_cli = subprocess.check_output('virsh net-list --all', shell=True)
    print(vnet_cli)

    
    subprocess.call('sleep '+'10', shell=True)
    #install vnc
    os.system('yum install firefox* gnome*')
    os.system('yum install vnc*')
    os.system('vncserver -list')
    os.system('vncserver -geometry 1840x940')
    
    
    try:
       subprocess.check_output('vncserver -list', shell=True)
    except subprocess.CalledProcessError as vncList:
       vncList.output.split()
    ar = vncList.output.split()
    if len(vncList.output.split()) > 8:
       os.system('echo vnc configuration successefully completed!')
       print(ar[8] + 'is your vnc port.')
       print('I recommend you launch your VNC GUI from the browser now so that you can\n use your virtual manager when the time comes. I will now wait for 30 seconds...')
    else:
       os.system('echo vnc configuration failed! Check your bridge configuration and other components.')
 
    subprocess.call('sleep '+'30', shell=True)
    build_conf = raw_input('Would you like me to build your Virtual Guests (y/n): ')
    if build_conf == 'y':
       src_host = 'c84f1u01:'
       src_dir = '/root/'
       src_file = 'vmguest.py'
       subprocess.call('scp '+src_host+src_dir+src_file+' '+'./', shell=True)
       subprocess.call('chmod +x '+src_file, shell=True)
       subprocess.call('./'+src_file, shell=True)
    else:
       os.system('echo Have a great day!') 
    

    subprocess.call('virsh list --all', shell=True)
    os.system('echo VM built successful!')      

# nmcli con modify enP3p9s0f0 master br0
# nmcli con edit bridge br0 # to edit the file
# help once in - this will show command structure
# nmcli con show --active

    
if __name__ == '__main__':
    main()
    

    
    
