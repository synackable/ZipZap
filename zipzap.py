#! /usr/bin/env python
# ZipZap - Written by @synackable | https://github.com/synackable/ZipZap


import os, sys, argparse, colorama, itertools
import zipfile, rarfile

argParseObj = argparse.ArgumentParser(description="ZipZap - Crack Compressed Files")

argParseObj.add_argument("--verbose", "-v", action="store_true", help="Enable verbose mode")

argParseFunctionVARGroup = argParseObj.add_argument_group("[Attack Config]")
argParseFunctionVARGroup.add_argument("--dictionary", "-d", required=False, help="Target dictionary to use against protected file (use 'auto' for predefined wordlist derived from SecLists")
argParseFunctionVARGroup.add_argument("--compfile", "-rf", help="Target compressed file to crack")
argParseFunctionVARGroup.add_argument("--genlist", "-gl", help="Generate all combinations of specified string to test against compressed file")
argParseFunctionVARGroup.add_argument("--genperm", "-gp", help="Generate all permutations of specified string to test against compressed file")

argParsedObj = argParseObj.parse_args()

def print_success(string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.GREEN}[+] ' + string + f'{colorama.Style.RESET_ALL}')
def print_warning(string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}[=] ' + string + f'{colorama.Style.RESET_ALL}')
def print_error(string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.RED}[-] ' + string + f'{colorama.Style.RESET_ALL}'); sys.exit(0)
def print_info(string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.CYAN}[i] ' + string + f'{colorama.Style.RESET_ALL}')
def print_debug(string):
    if argParsedObj.verbose: print (f'{colorama.Style.BRIGHT}{colorama.Fore.MAGENTA}[#] ' + string + f'{colorama.Style.RESET_ALL}')

def genPassList(tarStr):
    allCombos = [''.join(p) for p in itertools.permutations(tarStr)] # [''.join(l) for i in range(len(tarStr)) for l in itertools.combinations(tarStr, i+1)]
    with open('wordlist.txt', 'a') as wl:
        for combo in allCombos:
            wl.write(str(combo) + "\n")

def crackCompFile(tarRar, tarMode, tarDict=None, tarStr=None):
    # possible attack modes (tarMode) = dict, genperm, geniter
    if tarMode == "dict" and tarDict != None:
        for pw in tarDict:
            with rarfile.RarFile(tarRar, 'r') as rar:
                rar.extractall(pwd=pw)
    
    elif tarMode == "genperm" and tarStr != None:
        with rarfile.RarFile(tarRar) as rar:
            if rar.needs_password:
                for combo in itertools.permutations(tarStr):
                    try:
                        combo = ''.join(combo) # create full passwd to test
                        rar.setpassword(combo)
                        if len(rar.namelist()) > 0:
                            print_success("Password Found => " + str(combo)); sys.exit(0)
                    except Exception: pass
            else: print_error("This archive doesn't require a password goofy")

    elif tarMode == "geniter" and tarStr != None:
        print_info("Generating all possible iterations of {0}".format(tarStr))
    
    else: print_error("You didn't give a target dictionary or string :(")
    pass

if __name__ == '__main__':
    print_success("Welcome to ZipZap | Written by @synackable")

    if argParsedObj.compfile != None:
        if os.path.isfile(argParsedObj.compfile):
            print_info("Preparing to crack {0}..".format(argParsedObj.compfile)); print_debug("Compressed File Type: {0}".format(argParsedObj.compfile.split('.')[-1]))
            if argParsedObj.genperm != None:
                print_info("Generating all permutations of '{0}' to test against {1}..".format(argParsedObj.genperm, argParsedObj.compfile))
                crackCompFile(argParsedObj.compfile, 'genperm', tarStr=argParsedObj.genperm)

        else: print_error("Unfortunately {0} does not appear to exist. Please define a readable file".format(argParsedObj.compfile))
    else: print_error("Please define a compressed file to crack by appending '--compfile <file>'")