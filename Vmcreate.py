#! /usr/bin/python

import os
import subprocess
import shutil

def main():
 
    # Start at the Current working directory
    root_dir = os.getcwd()
    print("current directory is: "+ root_dir)
    subprocess.call('ls')

    # Create VM directory or make one.
    vm_dir = raw_input("Enter a vm directory name: ")
    print("you entered "+ vm_dir)
    try:
     os.mkdir(vm_dir)
    except OSError:
     print("Directory already exist!")
    else:
     print("You now have a vm directory: "+ vm_dir)
    
    # see the content of the the folder
    os.chdir(vm_dir)
    subprocess.call('ls')

    # Access the source folder from which to copy a VM file
    source_dir = raw_input("Enter the source folder from which to copy VM files: ")
    print("You have entered "+ source_dir)
    try:
     os.path.isdir(source_dir)
    except OSError:
     print("That source folder does not exist!")
    else:
     print("Accessing source directory...")

    os.chdir(source_dir)
    subprocess.call('ls')

    # Providing the desired VM file to be copied to the VM folder

    file_to_copy = raw_input("Enter the file to copy to your VM directory: ")
    try:
     os.path.isfile(file_to_copy)
    except OSError:
     print("The file you entered does not exist!")
    else:
     print("File entered succesfully! Copying over...")

    #copy file over and confirm it

    #subprocess.call('cp %s' % file_to_copy + '%s' % vm_dir, shell=True)
    shutil.copy(file_to_copy, vm_dir)
    # confirm content of vm dir
    os.chdir(vm_dir)
    subprocess.call('ls')

# Now we call the main function
if __name__ == '__main__':
   main()
