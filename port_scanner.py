import pyfiglet
import sys
import socket
from datetime import datetime

# Welcome Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Defining a target
target = input(str("Target IP : "))

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	
	# will scan ports between 1 to 65,535
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)
		
		# Return open port
		result = s.connect_ex((target,port))
		if result == 0:
			print("[*] Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()


# Possible upgrades 

#  - Create a list of common protocols and return the protocol that matches the port number
#  - use "threading" to make the scanner faster