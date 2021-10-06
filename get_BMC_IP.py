#! /usr/bin/python

import os
import subprocess
import shutil

def main():
    hostname = raw_input("Enter node name: ")
    os.system('host ' + hostname + 'bmc')

if __name__ == '__main__':
    main()
