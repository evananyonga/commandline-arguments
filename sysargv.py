# import system package
import sys, getopt


def main():
    sys_argv = sys.argv[1:]
    input_file = ''
    try:
        opts, args = getopt.getopt(sys_argv, 'hVo:i:v', ['help', 'version', 'output=', 'ifile='])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    # loop through the sys.argv options
    for f, a in opts:
        if f in ('-h', '--help'):
            help()
            sys.exit()
        elif f in ('-V', '--version'):
            print(sys.version)
        elif f in ('-o', '--output'):
            output = f
        elif f in ('-i', '--ifile'):
            input_file = f
            print('Input file is "', input_file)
        elif f in ('-v', '-vv'):
            verbose = True
            print(verbose)
        else:
            assert False, "unhandled option"


if __name__ == "__main__":
    main()
