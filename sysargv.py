# import system package
import sys


def main():
    sys_argv = sys.argv[1:]

    # loop through the sys.argv values
    for flag in sys_argv:
        if flag == '-help' or flag == '-h':
            help()
        elif flag in ('--version', '-V'):
            print(sys.version)
        elif flag in ('-v', '-vv'):
            verbose = True
            print(verbose)


if __name__ == "__main__":
    main()