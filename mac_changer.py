
import subprocess
import optparse
import re

def get_arguments():
    parser= optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options,get_arguments)=parser.parse_args()
     
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    return options

def mac_change(interface,new_mac):
    print("[+] Changing the mac address for "+ interface+" to "+ new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_currentMac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", options.interface])
    #print(ifconfig_result)
    mac_address_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("[-] I am unable to read its mac man, maybe its \"lo\" interface")
        


options=get_arguments()
current_mac=get_currentMac(options.interface)
mac=str(current_mac)

if not current_mac:
    print("Please check interface")
else:
    print("Current Mac is "+mac)

mac_change(options.interface,options.new_mac)
if(current_mac == options.new_mac):
    print("[+] Requested mac is changed successfully")
else:
    print("Oops!Sorry mac address not changed")
