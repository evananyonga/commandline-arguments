# A script that handles commandline arguments with sys.argv
# import os
import sys
import subprocess


def cl_args(*args):
    args = sys.argv[1:]
    for flag in args:
        if flag == '--help' or flag == '-h':
            print(help())
        else:
            subprocess.call([r'C:\Program Files\Git\\bin\\bash.exe', flag], shell=True)
        # if flag == '-v':
        #     print(sys.version)
        # elif flag == 'ls':
        #     print(os.listdir())
        # elif flag == 'dir':
        #     print(os.getcwd())
        # else:
        #     print('Command not found')


cl_args()
