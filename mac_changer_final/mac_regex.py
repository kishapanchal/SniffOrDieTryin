import subprocess
import optparse
import re 

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("please specify an interface , use --help for more information")
    elif not options.new_mac:
        parser.error("please specify a new mac , use --help for more information")
    return options

def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)

# decode bytes -> str (use system locale or explicit UTF-8)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface]).decode(errors="ignore")
print(ifconfig_result)

# robust MAC regex: hex pairs separated by colons (case-insensitive)
m = re.search(r"(?:[0-9a-f]{2}:){5}[0-9a-f]{2}", ifconfig_result, re.IGNORECASE)

if m:
    print(m.group(0))
else:
    print("[-] could not read mac address")