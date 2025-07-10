import socket

def scan_ports(host, ports):
    print(f"[+] Scanning {host}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} is OPEN")
                else:
                    print(f"Port {port} is CLOSED")
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")

if __name__ == "__main__":
    target_host = input("Enter target IP address: ")
    target_ports = [21, 22, 23, 80, 443, 8080]
    scan_ports(target_host, target_ports)
