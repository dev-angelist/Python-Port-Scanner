import socket

OPEN_PORTS = [] #List of open ports

def get_host_ip_addr(target):
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e:
        print(f"Error found: {e}")
    else:
        return ip_addr

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP/IPv4
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((ip, port)) #0 = open port, 1 = close_port
    if conn_status == 0:
        OPEN_PORTS.append(port)
    sock.close()

if __name__ == "__main__":
    target = input("Insert target: ")
    ip_addr = get_host_ip_addr(target)
    while True:
        try:
            port = int (input("Insert Port: "))
            scan_port(ip_addr, port)
            print(OPEN_PORTS)
        except KeyboardInterrupt: #Interrupt with CTRL+C
            print("\nExiting...")
            break
