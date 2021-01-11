# A script that handles commandline arguments with sys.argv
# import os
import sys
import glob
import getopt


def main():
    output = None
    verbose = False
    output = 'default.out'
    files = r'C:\Users\Ec\Downloads\Compressed\*.txt'
    sys_args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(sys_args, 'ho:v* .txt', ['help', 'output='])
    except getopt.GetoptError as err:
        err
        sys.exit(2)

    for flag, opt in opts:
        if flag == '-v':
            verbose = True
            print(verbose)
        elif flag in ('-h', '--help'):
            help()
            sys.exit()
        elif flag in ('-o', '--output'):
            output = opt
            print(output)
        elif flag in files:
            print(glob.glob(flag))
        else:
            assert False, 'unhandled option'
            # subprocess.call([r'C:\Program Files\Git\\bin\\bash.exe', flag], shell=True)
        # if flag == '-v':
        #     print(sys.version)
        # elif flag == 'ls':
        #     print(os.listdir())
        # elif flag == 'dir':
        #     print(os.getcwd())
        # else:
        #     print('Command not found')


if __name__ == '__main__':
    main()
