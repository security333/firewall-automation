import subprocess
import re
import socket

def resolve_ip(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return ip_address

def trace_route(destination):
    trace_output = subprocess.run(["traceroute", destination], capture_output=True, text=True)
    trace_lines = trace_output.stdout.splitlines()
    
    # Extract IPs from the traceroute output
    ip_addresses = [re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)[0] for line in trace_lines if re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)]
    
    # Resolve hostnames
    hostnames = [resolve_ip(ip) for ip in ip_addresses]
    
    # Print results
    print("Traceroute to", destination)
    for i, (ip, hostname) in enumerate(zip(ip_addresses, hostnames), start=1):
        print(f"{i}. {ip} ({hostname})")

if __name__ == "__main__":
    destination = input("Enter destination IP or domain: ")
    trace_route(destination)
