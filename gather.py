import subprocess
import re
import os

trace_counter = 1
ipv4_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  # Regex pattern for IPv4 addresses
ipv6_pattern = r"(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}"  # Regex pattern for IPv6 addresses

for addr in addresses:
    trace_incr = f"{trace_counter:03d}"
    hop_counter = 0

    if re.match(ipv4_pattern, addr):
        print(f"Please wait. Tracing route to {addr}...")
        with open(f"{working_ticket}/tmptrace-{trace_incr}.txt", "w") as f:
            subprocess.run(["traceroute", "-d", "-h", "15", "-w", "50", addr], stdout=f)

        with open(f"{working_ticket}/tmptrace-{trace_incr}.txt") as f:
            trace_results = f.read()
            ipv4_matches = re.findall(ipv4_pattern, trace_results)
            with open(f"{working_ticket}/tmptrace-{trace_incr}-extractedIPs.txt", "w") as out_f:
                for ip in ipv4_matches:
                    hop_incr = f"{hop_counter:02d}"
                    out_f.write(f"{trace_incr}-{hop_incr},{ip}\n")

    elif re.match(ipv6_pattern, addr):
        print(f"Please wait. Tracing route to {addr}...")
        with open(f"{working_ticket}/tmptrace-{trace_incr}.txt", "w") as f:
            subprocess.run(["traceroute", "-d", "-h", "15", "-w", "50", addr], stdout=f)

        with open(f"{working_ticket}/tmptrace-{trace_incr}.txt") as f:
            trace_results = f.read()
            ipv6_matches = re.findall(ipv6_pattern, trace_results)
            with open(f"{working_ticket}/tmptrace-{trace_incr}-extractedIPs.txt", "w") as out_f:
                for ip in ipv6_matches:
                    hop_incr = f"{hop_counter:02d}"
                    out_f.write(f"{trace_incr}-{hop_incr},{ip}\n")

    else:
        print(f"{addr} is not a valid IP address")
        # <# Action when this condition is true #>

# Combine extracted IPs from multiple files
with open(f"{working}/*-extratedIPs.txt", "r") as combined_file:
    extracted_ips = combined_file.read().strip().splitlines()

with open(f"{working_ticket}/extractedIPs-combined.txt", "w") as f:
    f.write("\n".join(filter(None, extracted_ips)))
