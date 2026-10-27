import subprocess
import re

# bu yangi mac manzilni tekshiradi
def get_mac(interface):
    result = subprocess.check_output(
        ["ifconfig", interface], text=True
    )
    match = re.search(r"ether ([\da-fA-F:]+)", result)
    return match.group(1) if match else None


interface = input("Enter interface: ")
new_mac = input("New MAC address: ")

if not re.fullmatch(r"(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", new_mac):
    print("[-] Invalid MAC address!")
    exit()

print("[+] Old MAC:", get_mac(interface))

try:
    subprocess.run(["ifconfig", interface, "down"], check=True)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
finally:
    subprocess.run(["ifconfig", interface, "up"])

print("[+] New MAC:", get_mac(interface))
