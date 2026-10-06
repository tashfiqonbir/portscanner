#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
import pyfiglet

# Banner
banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)
print("-" * 50)
print("     Coded by : TASHFIQ ONBIR")
print("     Use only for Educational Purpose ⚠️")
print("-" * 50)

# User input
target = input("\nEnter Target IP: ")

# Add banner
print(f"\nScanning Target: {target}")
print(f"Time Started: {datetime.now()}")
print("-" * 50)

try:
    # Scan ports 1 to 1000
    for port in range(1, 1001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3) # 0.3 sec wait
        
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} : OPEN")
        s.close()

except KeyboardInterrupt:
    print("\n[!] Exiting Program...")
    sys.exit()

except socket.gaierror:
    print("[!] Hostname Could Not Be Resolved!")
    sys.exit()

except socket.error:
    print("[!] Couldn't connect to server")
    sys.exit()

print("-" * 50)
print(f"Time Finished: {datetime.now()}")
print("Scan Complete!")