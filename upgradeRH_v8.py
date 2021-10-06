#! /usr/bin/python3
### RHEL upgrade
########################################################################
########################################################################
###                     author: Sunny Adeola                         ###
###                     email: osadeola@us.ibm.com                   ###
### Project: RHEL upgrade. Mainly for OS version using python V3.    ###
###          For OS versions using python v2 Please use the twin -   ###
###          upgradeRH_v3.py - found in /u/sunny/Tools or xcatmn3:   ###
########################################################################
########################################################################
import os
import subprocess
import shutil


def main():
    # 
     os.system('hostnamectl')
     
     os_class = {'RH7.6':['/u/admin/errata_repo/RH7.6/Kernel_errata_rh7_6_x86_64.repo','/u/admin/errata_repo/RH7.6/Kernel_errata_rh7_6_ppc64.repo','/u/admin/errata_repo/RH7.6/Kernel_errata_rh7_6_ppc64le.repo'], 'RH7.7':['/u/admin/errata_repo/RH7.7/Kernel_errata_rh7_7_x86_64.repo','/u/admin/errata_repo/RH7.7/Kernel_errata_rh7_7_ppc64.repo','/u/admin/errata_repo/RH7.7/Kernel_errata_rh7_7_ppc64le.repo'], 'RH7.8':['/u/admin/errata_repo/RH7.8/Kernel_errata_rh7_8_x86_64.repo','/u/admin/errata_repo/RH7.8/Kernel_errata_rh7_8_ppc64.repo','/u/admin/errata_repo/RH7.8/Kernel_errata_rh7_8_ppc64le.repo'], 'RH7.9':['/u/admin/errata_repo/RH7.9_release_cd/Kernel_errata_rh7_9_x86_64.repo','/u/admin/errata_repo/RH7.9_release_cd/Kernel_errata_rh7_9_ppc64.repo','/u/admin/errata_repo/RH7.9_release_cd/Kernel_errata_rh7_9_ppc64le.repo'], 'RH8.1':['/u/admin/errata_repo/RH8.1/Kernel_errata_rh8_1_x86_64.repo','/u/admin/errata_repo/RH8.1/Kernel_errata_rh8_1_ppc64le.repo'], 'RH8.2':['/u/admin/errata_repo/RH8.2/Kernel_errata_rh8_2_x86_64.repo','/u/admin/errata_repo/RH8.2/Kernel_errata_rh8_2_ppc64le.repo.repo'],'RH8.3':['/u/admin/errata_repo/RH8.3_release_cd/Kernel_errata_rh8_3_x86_64.repo','/u/admin/errata_repo/RH8.3_release_cd/Kernel_errata_rh8_3_ppc64le.repo'],'RH8.4':['/u/admin/errata_repo/192_network_repos/RH8.4/Kernel_errata_rh8_4_ppc64le_GA.repo','/u/admin/errata_repo/192_network_repos/RH8.4/Kernel_errata_rh8_4_x86_64_GA.repo']}
     for I in os_class.keys():
      print(I)

     node_os = input('Enter the target upgrade version as presented from above list: ')
    
#     for I in os_class[node_os]:
#      print(I)
     os.chdir('/u/admin/errata_repo/192_network_repos/'+ node_os +'/')
     os.system('ls')
     ugrade_repo = input('from the list above copy and paste here the os upgrade you require: ')
     
     shutil.copy(ugrade_repo, '/etc/yum.repos.d')
     os.chdir('/etc/yum.repos.d')

     os.system('ls')
     os.system('yum repolist')
     os.system('yum update')
    

     # confirm
     os.system('hostnamectl')
     
     power_stat = input('would you like to reboot (y/n): ')
     if power_stat == 'y':
      os.system('reboot')
     else:
      os.system('echo "your node is now successfully upgraded. You may need to restart for the new kernel to show up!"')
    # os.system('reboot')
        
       
if __name__ == '__main__':
    main()
