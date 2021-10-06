#! /usr/bin/python
### VM creation and setup

import os
import subprocess
import shutil

def main():
    # vm directory
    # Create VM directory or make one.
    # vm_dir = raw_input("Enter a vm directory name: ")
    #print("you entered "+ vm_dir)
    #try:
    # os.mkdir(vm_dir)
    #except OSError:
    # print("Directory already exist!")
    #else:
    # print("You now have a vm directory: "+ vm_dir)
    vm_dir = '/var/lib/libvirt/images'
    
    # copy over the required image file from c84f1u01
    # I am using dictionary as the data structure as I intend to add more arch per OS/key
    img_list = {'RH7.6':['RHEL-7.6-20181010.0-Server-x86_64-dvd1.iso','RHEL-7.6-20181010.0-Server-ppc64le-dvd1.iso'], 'RH7.7':['RHEL-7.7-20190723.1-Server-x86_64-dvd1.iso','RHEL-7.7-20190723.1-Server-ppc64-dvd1.iso'], 'RH7.9':['RHEL-7.9-20200917.0-Server-x86_64-dvd1.iso'], 'RH8.0':['RHEL-8.0.0-20190404.2-x86_64-dvd1.iso','RHEL-8.0.0-20190404.2-ppc64le-dvd1.iso'], 'RH8.1':['RHEL-8.1.0-20191015.0-x86_64-dvd1.iso',], 'RH8.2':['RHEL-8.2.0-20200404.0-x86_64-dvd1.iso','RHEL-8.2.0-20200404.0-ppc64le-dvd1.iso',], 'RH8.3':['RHEL-8.3.0-20201009.2-ppc64le-dvd1.iso'], 'SL15':['SLE-15-Installer-DVD-x86_64-GM-DVD1.iso'], 'SL15.1':['SLE-15-SP1-Installer-DVD-x86_64-GM-DVD1.iso'], 'SL15.2':['SLE-15-SP2-Full-x86_64-GM-Media1.iso'], 'UB16':['ubuntu-16.04.6-server-amd64.iso']}
    for keys in img_list.keys():
     print(keys)

    my_os = raw_input('Enter the OS to install on your VM from the above options: ')
     
    for I in img_list[my_os]:
     print(I)
    
    file_src = raw_input('Enter the node to copy image or iso file from: ')
    # access the vm directory to see if the image file is already there, if it is then provide no as the answer to the next question
    os.chdir(vm_dir)
    os.system('ls')
    
    img_Ask = raw_input('Would you like to copy over an image file: (y/n)')
    if img_Ask == 'y':
     iso_file = raw_input('Copy from the above list of iso files and paste here (e.g RHEL-7.6-20181010.0-Server-x86_64-dvd1.iso): ')
     subprocess.call('scp '+ file_src +':/root/power_kvm/'+iso_file + ' ./', shell=True)
    else:
     iso_file = raw_input('Copy from the above list of iso files and paste here (e.g RHEL-7.6-20181010.0-Server-x86_64-dvd1.iso): ')
    #subprocess.call('scp prh03:/root/os_list '+'./', shell=True)
    node_arch = raw_input('Enter your vm architecture (e.g x86_64): ')
    rawfile_name = my_os+'.'+node_arch+'.raw'
    disk_name = my_os+'.'+node_arch+'.qcow2'
    subprocess.check_output('qemu-img convert -O raw '+iso_file+' '+rawfile_name, shell=True)
    subprocess.check_output('qemu-img convert -O raw '+rawfile_name+' '+disk_name, shell=True)
    #os.chdir('/root/')
    
    # Now we begin to add parameters that add up to our guest
    # first we want to make sure the hos name is in the /etc/host file
    os.system('virsh list --all')
    os.system('cat /etc/hosts')
    vm_name = raw_input('Copy from the above list of names and paste here: (Note: avoid recreating VMs) ')
    ram_size = raw_input('Provide your desired RAM size (e.g 40960): ')
    #os.chdir(vm_dir)
    os.system('pwd')
    os.system('ls')
    disk_path = raw_input('Provide the path to your image (e.g /root/powerkvm/rhel76.x86_64.qcow2): ')
    disk_size = raw_input('Enter your storage size here: (e.g 40): ')
   # stg_size = int(disk_size)
    Vcpus = raw_input('Enter the desired number of virtual CPUs (e.g 2,1 etc): ')
   # V_cpu = int(Vcpus)
    Os_type = raw_input('Enter your os type (e.g linux): ')
    #os_l = subprocess.call('cat os_list', shell=True)
    os_Variant = raw_input('Provide your desired os from the above list (e.g rhel7.9: ')
    network_path = 'http://192.168.180.242:80/install/'
   # node_arch = raw_input('Enter your node architecture (e.g x86_64): ')
    vnet_int = raw_input('Enter your virtual bridge interface (e.g br0 ): ')
    subprocess.call('host ' + vm_name, shell=True)
    vm_ipAddr = raw_input('Enter the VM IP indicated above: ')
    nic_int = raw_input('Enter desired network interface for your vm (e.g eth0): ')

    subprocess.call('virt-install ' + '--name '+ vm_name + ' --ram ' + ram_size + ' --disk path=' + disk_path + ',size=' + disk_size + ' --vcpus ' + Vcpus + ' --os-type ' + Os_type + ' --os-variant ' + os_Variant + ' --location ' + network_path + os_Variant + '/' + node_arch + ' --network bridge='+vnet_int + ' --extra-args ' + '"ip='+vm_ipAddr+'::192.168.180.247:255.255.0.0:'+vm_name+'.gpfs.net'+':'+nic_int+':none"', shell=True) 
    
    # manage the .xml file generated from your virtual guest by moving it to the virtual directory.
    #subprocess.call('virsh dumpxml '+vm_name + ' | tee '+vm_name+'.xml', shell=True)
    xml_file = subprocess.check_output('virsh dumpxml '+vm_name + ' | tee '+vm_name+'.xml', shell=True)
    shutil.copy(xml_file, vm_dir)
 
    # confirm it has been moved
    #os.chdir(vm_dir)
    os.getcwd()
    os.system('ls')
      
    
    
     
     
    
    


if __name__ == '__main__':
   main()

    
     
