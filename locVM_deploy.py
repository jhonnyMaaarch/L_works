#! /usr/bin/python
########################################################################
########################################################################
###                     author: Sunny Adeola                         ###
###                     email: osadeola@us.ibm.com                   ###
### project: Module will create Fileset. link the fileset and create ###
### VM(s) according to use spec                                      ###
###                                                                  ###
########################################################################
########################################################################
import os
import subprocess
import shutil

# Function indicating the working directory
def currWorkDir(S_dir):
    S_dir = os.getcwd()
    print ("current directory is:"+ S_dir)
    return S_dir


# This will be the directory in which all the vm files such as .iso, .xml etc resides
# This will be the function that creates the VM files
# It will ask for a VM directory. If one exist it will confirm it, if not, it will create it
def VM_dir(vm_workdir):
    vm_workdir =  raw_input("Enter name of directory to be used for VM files: ")
    print ("you entered : " + vm_workdir)
#    os.path.isdir(vm_workdir)
#    path = vm_workdir
    try:
      os.mkdir(vm_workdir)
    except OSError:
      print("creation of directory %s failed, directory already exist" % vm_workdir)
    else:
      print("Successfully created directory %s" % vm_workdir)
    return vm_workdir


# This function will ask for the source folder wherein resides the VM files

def target_Folder(targ_folder):
    targ_folder = raw_input("Enter the target folder from which to copy needed VM files: ")
    try:
     os.path.isdir(targ_folder)
    except OSError:
      print("There is no such directory!")
    else:
      print("You have entered %s" % targ_folder)
    return targ_folder

# This is the function that asks for the file to be copied and the copy it from current directory to 
# the destination 1.e VM directory
def vm_file(file_to_copy):
    file_to_copy = raw_input("Enter the file to be copied: ")
    try:
     os.path.isfile(file_to_copy)
    except OSError:
     print("There is no such file in this directory!")
    else:
     print("Your file is %s" % file_to_copy)
    return file_to_copy

# Calling the function that shows us our current working directory
S_dir = "" # initialize d var to be provided as arg to d currWorkDir
currWorkDir(S_dir)
subprocess.call('ls')

# Calling the function that makes or provides our vm directory
vm_workdir = ""
VitualDir = VM_dir(vm_workdir)
os.chdir(VitualDir)
subprocess.call('ls')

# calling the function that links us to the sources directory from which to copy VM files
targ_folder = ""
source_folder = target_Folder(targ_folder)
os.chdir(source_folder)
subprocess.call('ls')

# list the files in the source directory 
num = os.listdir(source_folder)
print(num)

# copy file from source directory to destination or vm directory
file_to_copy = ""
config_file = vm_file(file_to_copy)
#subprocess.call('cp %s' % file_to_copy + '%s' % VitualDir, shell=True)
shutil.copy(config_file, VitualDir)

#confirm that you have copied file successfully
os.chdir(VitualDir)
subprocess.call('ls')
