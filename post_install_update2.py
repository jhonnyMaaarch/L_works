#! /usr/bin/python
####This will be the python module for OS install
import os
import subprocess
import shutil

def main():
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
    
#    FileName = raw_input("Enter file name (e.g hostname: ")
    FileName = "hostname"
    CreateFile = open (FileName, 'w+')
    CreateFile.write(host_name)
    CreateFile.write("\n")
    print(CreateFile.read())
    CreateFile.close()
    
    os.system('cat /etc/hostname')

#   configure repository
    os.chdir('/etc/yum.repos.d/')
    
    os_version = raw_input("Enter the OS version installed (e.g rh7.6): ")
   # os_arch = subprocess.check_output('uname -i', shell=True)
    os.system('uname -i')
    os_arch = raw_input("Enter the hardware architecture (e.g ppc64): ")
    print("hw architecture is "+ os_arch)
    if os_version == "rh7.6" and os_arch == "x86_64":
       os.system("scp xcatmn3:/u/admin/errata_repo/RH7.6/Kernel_errata_rh7_6_x86_64.repo ./")
    elif os_version == "rh7.6" and os_arch == "ppc64":
       os.system("scp xcatmn3:/u/admin/errata_repo/RH7.6/Kernel_errata_rh7_6_ppc64.repo ./")
    elif os_version == "rh7.6" and os_arch == "ppc64le":
       os.system("scp xcatmn3:/u/admin/errata_repo/RH7.6/Kernel_errata_rh7_6_ppc64le.repo ./")
    else:
       if os_version == "rh7.7" and os_arch == "x86_64":
          os.system("scp xcatmn3:/u/admin/errata_repo/RH7.7/Kernel_errata_rh7_7_x86_64.repo ./")
       elif os_version == "rh7.7" and os_arch == "ppc64":
          os.system("scp xcatmn3:/u/admin/errata_repo/RH7.7/Kernel_errata_rh7_7_ppc64.repo ./")
       elif os_version == "rh7.7" and os_arch == "ppc64le":
          os.system("scp xcatmn3:/u/admin/errata_repo/RH7.7/Kernel_errata_rh7_7_ppc64le.repo ./")
       else:
          if os_version == "rh7.8" and os_arch == "x86_64":
             os.system("scp xcatmn3:/u/admin/errata_repo/RH7.8/Kernel_errata_rh7_8_x86_64.repo ./")
          elif os_version == "rh7.8" and os_arch == "ppc64":
             os.system("scp xcatmn3:/u/admin/errata_repo/RH7.8/Kernel_errata_rh7_8_ppc64.repo ./")
          elif os_version == "rh7.8" and os_arch == "ppc64le":
             os.system("scp xcatmn3:/u/admin/errata_repo/RH7.8/Kernel_errata_rh7_8_ppc64le.repo ./")
          else:
             if os_version == "rh8.1" and os_arch == "x86_64":
                os.system("scp xcatmn3:/u/admin/errata_repo/RH8.1/Kernel_errata_rh8_1_x86_64.repo ./")
             elif os_version == "rh8.1" and os_arch == "ppc64":
                os.system("scp xcatmn3:/u/admin/errata_repo/RH8.1/Kernel_errata_rh8_1_ppc64.repo ./")
             elif os_version == "rh8.1" and os_arch == "ppc64le":
                os.system("scp xcatmn3:/u/admin/errata_repo/RH8.1/Kernel_errata_rh8_1_ppc64le.repo ./")
             else:
                if os_version == "rh8.2" and os_arch == "x86_64":
                   os.system("scp xcatmn3:/u/admin/errata_repo/RH8.2/Kernel_errata_rh8_2_x86_64.repo ./")
                elif os_version == "rh8.2" and os_arch == "ppc64":
                   os.system("scp xcatmn3:/u/admin/errata_repo/RH8.2/Kernel_errata_rh8_2_ppc64.repo ./")
                elif os_version == "rh8.2" and os_arch == "ppc64le":
                   os.system("scp xcatmn3:/u/admin/errata_repo/RH8.2/Kernel_errata_rh8_2_ppc64le.repo ./")
                else:
                   os.system("That repository is NOT available at this time!")
    

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
             pubg_way = "9.114.180.247"
             os.system("ifconfig " + net_interface + " " + pub_ip + " netmask " + pub_net + " broadcast " + pub_bCast)
             os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')  
             p_ifcfg_file = ('ifcfg-'+net_interface)
             CreateFile = open(p_ifcfg_file, 'w+')
             CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + pub_ip + '\n' + 'NETMASK=' + pub_net + '\n' + 'GATEWAY=' + pubg_way)
             CreateFile.write("\n")
             print(CreateFile.read())
             CreateFile.close()
       else: 
             ip_list = []
             private_ip_finder = subprocess.check_output('hostname -i', shell=True)
             private_ip_finder1 = str(private_ip_finder)
             ip_list = private_ip_finder1.split()
             print(ip_list)
             private_ip = ip_list[4]
             private_net ='255.255.0.0'
             privateg_way ='192.168.255.254'
             os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')
             ifcfg_file = ('ifcfg-'+net_interface)
             CreateFile = open(ifcfg_file, 'w+')
             CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + private_ip + '\n' + 'NETMASK=' + private_net + '\n' + 'GATEWAY=' + privateg_way)
             CreateFile.write('\n')
             print(CreateFile.read())
             CreateFile.close()

       os.system('cp -p ifcfg-'+net_interface + " " + 'ifcfg-'+net_interface+'_orig')  
       ifcfg_file = ('ifcfg-'+net_interface)
       CreateFile = open(ifcfg_file, 'w+')
       CreateFile.writelines('###ifcfg-'+net_interface + '\n' + 'DEVICE='+net_interface + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + private_ip + '\n' + 'NETMASK=' + private_net + '\n' + 'GATEWAY=' + privateg_way)
       CreateFile.write('\n')
       print(CreateFile.read())
       CreateFile.close()
    os.system('ls')
    os.system('ifconfig') 

if __name__ == '__main__':
    main()
