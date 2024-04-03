import subprocess
import re
import os

# (?:[a-fA-F0-9]{1,4}:){3,7}(?:::[a-fA-F0-9]{1,4})?


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
                
