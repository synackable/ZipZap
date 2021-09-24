#! /usr/bin/env python
# ZipZap - Written by @synackable | https://github.com/synackable/ZipZap


import sys, argparse, colorama

argParseObj = argparse.ArgumentParser(description="DTW API (and beyond) Controller - A hacky method to working with DefendTheWeb(.net)!")

argParseObj.add_argument("--verbose", "-v", action="store_true", help="Enable verbose mode")

argParseFunctionVARGroup = argParseObj.add_argument_group("[Attack Config]")
argParseFunctionVARGroup.add_argument("--dictionary", "-d", required=False, help="Target dictionary to use against protected file (use 'auto' for predefined wordlist derived from SecLists")
argParseFunctionVARGroup.add_argument("--tor", "-t", help="Enable Tor Proxy Routing (syntax: --tor 9050)")

argParsedObj = argParseObj.parse_args()

def print_success( string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.GREEN}[+] ' + string + f'{colorama.Style.RESET_ALL}')
def print_warning( string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}[=] ' + string + f'{colorama.Style.RESET_ALL}')
def print_error( string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.RED}[-] ' + string + f'{colorama.Style.RESET_ALL}'); sys.exit(0)
def print_info( string): print (f'{colorama.Style.BRIGHT}{colorama.Fore.CYAN}[i] ' + string + f'{colorama.Style.RESET_ALL}')
def print_debug( string):
    if argParsedObj.verbose: print (f'{colorama.Style.BRIGHT}{colorama.Fore.MAGENTA}[#] ' + string + f'{colorama.Style.RESET_ALL}')



if __name__ == '__main__':
    print_success("Welcome to ZipZap | Written by @synackable")