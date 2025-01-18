import socket

def scan_ports(target, ports):
	open_ports = []
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		result = sock.connect_ex((target, port))
		if result == 0:
			open_ports.append(port)
		sock.close()
	return open_ports

def main():
	target_host = input("Enter the target host to scan: ")
	target_ports = range(1, 1025)  # Scan common ports (1-1024)
	
	open_ports = scan_ports(target_host, target_ports)
	
	if open_ports:
		print("Open ports on {}: {}".format(target_host, open_ports))
	else:
		print("No open ports found on {}".format(target_host))
		
if __name__ == "__main__":
	main()
	
