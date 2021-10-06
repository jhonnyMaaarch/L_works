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


if __name__ == '__main__':
   main()
