#! /usr/bin/python
####This will be the python module for OS install
import os
import subprocess
import shutil

def main():
    # configure password
    password = raw_input('Would you like to configure password (Y or N): ')
    if password == "Y":
        passwd = subprocess.check_output('passwd', shell=True)
    else:
        os.system('proceeding...')
   

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
    
    #dns configuration
    os.system('scp 192.168.180.24:/etc/resolv.conf /etc/resolv.conf')
    os.system('cat /etc/resolv.conf')

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

#   configure repository
    os.system('host ftp3.linux.ibm.com')
    #print(ext_repo)
    os.system('route add -net ' + 'default' + ' netmask ' + '255.255.255.0' + ' gw ' + '9.114.180.254')
    os.system('route')
    os.chdir('/root')
    os_arc = subprocess.check_output('uname -i', shell=True)
    print("OS architecture is " + os_arc )
    os_arch = raw_input("Enter the hardware architecture above (e.g ppc64): ")
    if os_arch == "ppc64":
       os.system('scp -p xcatmn3:ibm-yum.sh ./')
       os.system('./ibm-yum.sh')
    elif os_arch == "ppc64le":
       os.system('scp -p xcatmn3:ibm-yum.sh ./')
       os.system('./ibm-yum.sh')
    elif os_arch == "x86_64":
       os.system('scp -p xcatmn3:ibm-rhsm.sh ./')
       os.system('./ibm-rhsm.sh')
    else:
        os.system('No defined repository')
    
    print("current directory is: "+ root_dir)
    os.chdir('/etc/yum.repos.d/')
    os.system('ls')    

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
    

    #copy over auto.master file - the automount master file for specifying directories to be controlled along with their corresponding map files.
    os.system('scp xcatmn3:/u/admin/master_files/auto.master.linux /etc/auto.master')
    
    # copy over the auto.u - the actual u file with users directories
    os.system('scp xcatmn3:/u/admin/master_files/auto.u.master /etc/auto.u')
    
    # start nfs service
    os.system('chkconfig --level 2345 nfs on')
    # start autofs service
    os.system('chkconfig --level 2345 autofs on')
    # systemctl start nfs-server.service
    os.system('systemctl start nfs.service')
    os.system('systemctl start autofs.service')
    os.system('ls /u/shujun')
    
    # initiate the xinetd activation process - xinetd is the daemon that starts services that provide internet services
    os.system('cd /u/shujun/scripts')
    os.system('cp rsh-rh.tar /etc/xinetd.d')
    os.system('cd /etc/xinetd.d')
    os.system('tar xvf rsh-rh.tar')
    os.system('service xinetd stop')
    os.system('service xinetd start')
    
    # setup time
    os.system('/u/gpfstest/network/NTP/setupntp.linux')

    # configure network interface
    os.chdir('/etc/sysconfig/network-scripts')
    os.system('ls')
    os.system('ifconfig')
    
    num_int = raw_input("How many interface would you like to configure: ") 
    num_interface = int(num_int)
    counter = 0
    

    for counter in range(num_interface):
       net_interface = raw_input("Enter the interface to be configured (e.g "+" eno" + str(counter) + ")" ) 
       int_type = raw_input("Is this the public interface (Y or N): ")
       if int_type == 'Y':
             pub_hostname = subprocess.check_output('host ' + host_name + ".pok.stglabs.ibm.com", shell=True)
             print(pub_hostname)
             pub_ip = raw_input("Enter the IP indicated above: ")
             pub_net = "255.255.255.0"
             pub_bCast = "9.114.180.255"
             pubg_way = "9.114.180.254"
             os.system("ifconfig " + net_interface + " " + pub_ip + " netmask " + pub_net + " broadcast " + pub_bCast)
             os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')  
             p_ifcfg_file = ('ifcfg-'+net_interface)
             CreateFile = open(p_ifcfg_file, 'w+')
             CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + pub_ip + '\n' + 'NETMASK=' + pub_net + '\n' + 'GATEWAY=' + pubg_way)
             CreateFile.write("\n")
             print(CreateFile.read())
             CreateFile.close()
       elif int_type == 'N': 
             ip_list = []
             private_ip_finder = subprocess.check_output('hostname -i', shell=True)
             my_str = str(private_ip_finder)
             ip_list = my_str.split()
             print(ip_list)
             for I in ip_list:
                right_IP = raw_input('is '+ I + ' your IP: (Y or N) ' )
                if right_IP == "Y":
                    private_ip = I
                elif private_ip != I:
                    private_ip == '192.168.180.X'
                else:
                    os.system('IP not listed')

             private_net ='255.255.0.0'
             privateg_way ='192.168.180.247'
             os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')
             ifcfg_file = ('ifcfg-'+net_interface)
             CreateFile = open(ifcfg_file, 'w+')
             CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + private_ip + '\n' + 'NETMASK=' + private_net + '\n' + 'GATEWAY=' + privateg_way)
             CreateFile.write('\n')
             print(CreateFile.read())
             CreateFile.close()
       else:
             os.system('ls')
             os.system('ifconfig')
    os.system('ls')
    os.system('ifconfig') 
    
    # Activate syslog
    os.system('mv -f  /etc/rsyslog.conf /etc/rsyslog.conf.orig')
    os.system('mv -f  /etc/rsyslog.conf.XCATORIG /etc/rsyslog.conf')
    os.system('service rsyslog stop')
    os.system('service rsyslog start')
    os.system('ls -l /var/log/messages')

if __name__ == '__main__':
    main()
