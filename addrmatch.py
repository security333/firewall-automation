import subprocess
import re
import os

ipv6_pattern = (
    r'('
    # Full IPv6 address with all eight groups separated by colons
    r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
    r'|'
    # IPv6 address with double colon abbreviation (e.g., ::1)
    r'((([0-9a-fA-F]{1,4}:){1,6})|::)(([0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?'
    r'|'
    # IPv6 address with leading zeros in each group omitted (e.g., 2001:db8::1)
    r'([0-9a-fA-F]?::[0-9a-fA-F]{1,4})|([0-9a-fA-F]{1,4}::[0-9a-fA-F]{1,4})'
    r'|'
    # IPv6 address with IPv4-mapped IPv6 address representation (e.g., ::ffff:192.0.2.1)
    r'(::ffff:((0{0,3}\d|0x[0-9a-fA-F]{1,2})\.){3}(0{0,3}\d|0x[0-9a-fA-F]{1,2}))'
    r')'
)


ipv4 = "ipv4_regex_pattern"  # Define your IPv4 regex pattern
addresses = ["address1", "address2", "address3"]  # Example list of addresses

working_ticket = "your_working_ticket_directory_path"  # Specify your working ticket directory path

for addr in addresses:
    if re.match(ipv4, addr):
        print(f"please wait. Tracing route to {addr}...")
        trace_output = subprocess.run(["tracert", "-d", "-h", "15", "-w", "50", addr], capture_output=True, text=True)
        
        with open(os.path.join(working_ticket, f"tmptrace-{trace_incr}.txt"), "w") as file:
            file.write(trace_output.stdout)
        
        trace_results = trace_output.stdout
        extracted_ips = re.findall(ipv4, trace_results)
        
        with open(os.path.join(working_ticket, f"tmptrace-{trace_incr}-extractedIPs.txt"), "w") as file:
            for hop_counter, ip in enumerate(extracted_ips, start=1):
                hop_incr = f"{hop_counter:02}"
                file.write(f"{trace_incr}-{hop_incr}, {ip}\n")
                
