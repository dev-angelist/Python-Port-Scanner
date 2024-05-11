import pyfiglet
import sys
import socket
from datetime import datetime
import os
import argparse

def print_banner(message):
    #Prints a banner with a message.
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message))

def print_section_header(message, char='-'):
    #Prints a section header with a specified character.
    print("\n" + char * len(message))
    print(message)
    print(char * len(message))

def parse_ip_list(ip_list):
    #Parse IP addresses from input list.
    ips = []
    for item in ip_list:
        # Check if the item is a file
        if os.path.isfile(item):
            with open(item, 'r') as file:
                ips.extend([ip.strip() for ip in file.read().splitlines() if ip.strip()])
        else:
            ips.extend(item.split(','))
    return ips

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Port Scanner - Scan for open ports on specified IP addresses.')
parser.add_argument('-i', '--ip', metavar='IP', type=str, nargs='+', help='Target IP addresses separated by comma or space.')
parser.add_argument('-f', '--file', metavar='FILE', type=str, help='Read target IP addresses from a file.')
parser.add_argument('-o', '--output-dir', metavar='DIRECTORY', type=str, help='Directory to save output files (if not defined will be the current path).')
args = parser.parse_args()

# Check if IP addresses are provided
if not (args.ip or args.file):
    # Print help message and request to provide IP addresses
    print("Please provide IP addresses as arguments or use the -help flag for more information.")
    print("\nExamples: python3 scan.py -i 127.0.0.1\n\t  python3 scan.py -i 127.0.0.1, 172.17.0.2\n\t  python3 scan.py -f list_ip.txt -o /home/kali/Documents")
    sys.exit()

# Read IP addresses from file if provided
if args.file:
    with open(args.file, 'r') as file:
        targets = [line.strip() for line in file.readlines() if line.strip()]
else:
    targets = parse_ip_list(args.ip)

# Remove empty IP addresses
targets = [ip for ip in targets if ip]

# Generate ASCII art banner for the port scanner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font = "slant")
print(ascii_banner)

# Print scanning information
print_section_header(f"Scanning Targets: {', '.join(targets)}")
print_section_header(f"Scanning started at: {str(datetime.now())}")

open_ports = {}  # Dictionary to store open ports for each IP address

try:
    # Iterate over each target IP address
    for idx, target in enumerate(targets, 1):
        target = target.strip()  # Remove any leading or trailing spaces from the IP address
        open_ports[target] = []  # Initialize an empty list to store open ports for the IP address
        print_section_header(f"Scanning Target ({idx}/{len(targets)}): {target}", char='*')
        total_ports = 65535
        ports_scanned = 0
        ports_found = False
        # Try to connect to the target IP address
        try:
            # Attempt to establish a connection to the target IP address with a timeout of 3 seconds
            s = socket.create_connection((target, 80), timeout=3)
            s.close()
        except (socket.timeout, ConnectionRefusedError, socket.gaierror):
            # Handle timeout, connection refused, or DNS resolution error
            print_section_header(f"[x] Failed to connect to {target}. Please check the IP address and try again.", char='-')
            continue  # Skip to the next target

        # Iterate over each port (from 1 to 65535) and attempt to connect
        for port in range(1, total_ports + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Set a timeout of 1 second for the connection attempt

            # Attempt to connect to the port on the target IP address
            result = s.connect_ex((target, port))
            ports_scanned += 1
            # If the connection attempt is successful (result is 0), mark the port as open
            if result == 0:
                open_ports[target].append(port)  # Add the open port to the list for the corresponding IP address
                ports_found = True
                print(f"[+] Port {port} is open")
            s.close()

        # If open ports are found for the target, save the list to a file
        if ports_found:
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
            ip_address = target.replace(".", "-")
            if args.output_dir:
                file_path = os.path.join(args.output_dir, f"open_ports_{ip_address}_{date_time}.txt")
            else:
                file_path = f"open_ports_{ip_address}_{date_time}.txt"
            try:
                # Try to save the output file
                with open(file_path, "w") as file:
                    for port in open_ports[target]:
                        file.write(str(port) + "\n")
                print_banner(f"[v] Open ports list for {target} saved to file '{file_path}'", )
            except PermissionError:
                # If permission error occurs, print the results to screen
                print_banner(f"[x] Permission denied. Unable to save open ports list for {target}. Printing to screen instead:")
                for port in open_ports[target]:
                    print(port)
        else:
            # If no open ports are found for the target, display a message
            print_section_header(f"[x] No open ports found for {target}. The castle remains unbreachable!", char='-')

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("\n[x] Exiting Program!!")
    sys.exit()
except socket.error:
    # Handle socket error
    print("\n[x] Server not responding!!")
    sys.exit()
