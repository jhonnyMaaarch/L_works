#! /usr/bin/python
####This will be the python module for OS install
import os
import subprocess
import shutil

def main():
    # provide password
    passd = raw_input('Would you like to provide a password (y/n): ')
    if passd == 'y':
      passwd = subprocess.call('passwd', shell=True)
    else:
      os.system('echo continue')

    # configure the hostname
    host_name = subprocess.check_output('hostname -s', shell=True)
    my_hname = []
    my_hname.append(host_name)
    for h_name in my_hname:
      print('you hostname will be '+h_name)
    os.chdir('/etc/')
    host_Filename = 'hostname'
    CreateFile = open(host_Filename, 'w+')
    CreateFile.write(h_name)
    CreateFile.write('\n')
    CreateFile.read()
    CreateFile.close()
   
    # configure dns
    net_domain = 'gpfs.net'
    name_server = '192.168.180.253'
    name_server2 = '9.12.16.2'
    dns_file = 'resolv.conf'
    CreateFile = open(dns_file, 'w+')
    CreateFile.writelines('domain '+net_domain + '\n' + 'nameserver '+name_server + '\n' + 'nameserver2 ' +name_server2)
    CreateFile.write('\n')
    CreateFile.read()
    CreateFile.close()
    

    # configure the route
    or_gw = h_name+'.gpfs.net'
    os.system('ifconfig')
    Def_gw = '9.114.180.254'
    os.system('route')
    subprocess.call('route add -net default netmask 0.0.0.0 gw '+Def_gw, shell=True)
    subprocess.call('route del -net default netmask 0.0.0.0 gw '+or_gw, shell=True)
    os.system('route')
    
    arch_class={'x86_64':'/root/ibm-rhsm.sh', 'ppc64':'/root/ibm-yum.sh', 'ppc64le':'/root/ibm-yum.sh'}
    
    arch = subprocess.check_output('uname -m', shell=True)
    my_arch = []
    my_arch.append(arch)
    for arch_prof in my_arch:
      print('Node architecture is '+arch_prof)
    node_arch = raw_input('copy and paste the node architecture here: ')
    if node_arch == 'x86_64':
      subprocess.call('scp c20xcatmn3:/root/ibm-rhsm.sh ./', shell=True)
      subprocess.call('chmod +x ibm-rhsm.sh', shell=True)
      subprocess.call('./ibm-rhsm.sh', shell=True)
    elif node_arch == 'ppc64':
      subprocess.call('scp prh03:/root/ibm-yum.sh', shell=True)
      subprocess.call('chmod +x ibm-yum.sh', shell=True)  
      subprocess.call('./ibm-yum.sh', shell=True)
    elif node_arch == 'ppc64le':
      subprocess.call('scp prh03:/root/ibm-yum.sh', shell=True)
      subprocess.call('chmod +x ibm-yum.sh', shell=True)
      subprocess.call('./ibm-yum.sh', shell=True)
    else:
      subprocess.call('echo related repository not yet available!', shell=True)

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
    
    # Configure network interface
    subprocess.call('ifconfig')
    nic_interface = raw_input('How many interface would you like to configure: ')
    nic_int = int(nic_interface)
    pub_hName = h_name+'.gpfs.net'
    for nic in range(nic_int):
      nic_nm = raw_input('Enter the nic to be configured: ')
      nic_Type = raw_input('Is this the punlic NIC (y/n): ')
      if nic_Type == 'y':
        publ_ip = subprocess.call('host '+pub_hName, shell=True)
        p_ipaddr=publ_ip.split()
        p_ip = p_ipaddr[3]
        p_NET='255.255.255.0'
        p_brdcat='9.114.180.255'
        subprocess.call('ifconfig ' + nic_nm + '' + p_ip + ' netmask ' + p_NET + ' broadcast ' + p_brdcat, shell=True)
        os.chdir('/etc/sysconfig/network_scripts')
        nic_File = 'ifcfg-'+nic_nm
        os.system('cp -p '+nic_File + ' ' + nic_File+'_orig')
        CreateFile = open(nic_File, 'w+')
        CreateFile.writelines('###ifcfg-'+nic_nm + '\n' + 'DEVICE='+nic_nm + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + p_ip + '\n' + 'NETMASK=' + p_NET + '\n' + 'GATEWAY=' + Def_gw)
        CreateFile.write('\n')
        CreateFile.read()
        CreateFile.close()
        subprocess.call('cat '+ nic_File, shell=True)
        os.system('ls')
      else:
        private_ip = subprocess.call('host '+or_gw, shell=True)   
        priv_IP = private_ip.split()
        pr_addr = priv_IP[3]
        p_NET='255.255.0.0'
        p_bcast = '192.168.255.255'
        private_gw = '192.168.180.247'
        os.chdir('/etc/sysconfig/network_scripts')
        nic_File = 'ifcfg-'+nic_nm
        os.system('cp -p '+nic_File + ' ' + nic_File+'_orig')
        CreateFile = open(nic_File, 'w+')
        CreateFile.writelines('###ifcfg-'+nic_nm + '\n' + 'DEVICE='+nic_nm + '\n' + 'BOOTPROTO=static' + '\n' + 'STARTMODE=onboot' + '\n' + 'ONBOOT=yes' + '\n' + 'IPADDR=' + pr_addr + '\n' + 'NETMASK=' + p_NET + '\n' + 'GATEWAY=' + private_gw)
        CreateFile.write('\n')
        CreateFile.read()
        CreateFile.close()
        subprocess.call('cat '+ nic_File, shell=True)
        os.system('ls')


        os.system('echo node install and configuration now concluded!')

if __name__ == '__main__':
   main()



