import csv

# Function to remove duplicates from a list while preserving the order
def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

# Read IP addresses from the text file
with open('input.txt', 'r') as file:
    ip_addresses = file.readlines()

# Remove duplicates
unique_ip_addresses = remove_duplicates(ip_addresses)

# Write unique IP addresses to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for ip in unique_ip_addresses:
        writer.writerow([ip.strip()])
