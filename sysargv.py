# import system package
import getopt
import sys


def main():
    sys_argv = sys.argv[1:]
    input_file = ''
    try:
        opts, args = getopt.getopt(sys_argv, 'hVo:i:v', ['help', 'version', 'output=', 'ifile='])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    # loop through the sys.argv options
    for arg, opt in opts:
        if arg in ('-h', '--help'):
            help()
            sys.exit()
        elif arg in ('-V', '--version'):
            print(sys.version)
        elif arg in ('-o', '--output'):
            output = arg
        elif arg in ('-i', '--ifile'):
            input_file = arg
            print('Input file is "', input_file)
        elif arg in ('-v', '-vv'):
            verbose = True
            print(verbose)
        else:
            assert False, "unhandled option"


if __name__ == "__main__":
    main()
