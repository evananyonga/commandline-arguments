# Command line arguments with sysargv and argparse 
## This programme contains two python scripts
#### 1. A script that tests out the command line with the sys.argv method
#### 2. A script that tests out the command line with the argparse method

### The outcome for both scripts
* Both scripts handle the -help or -h command
* Both scripts will also handle other flags like:
    * python version ie; --version, -V
    * verbose ie; -v, -vv
* Both scripts should be able to handle arguments that are options ie they take other arguments and set the variable in the script to that option like:
  * -o and --output
  * -i and --ifile