import requests
import json

# Define the URL
url = 'https://nstest.com'

# Start a session
session = requests.Session()

# Send a GET request to the URL and store the response in contact_nsd
contact_ghn = session.get(url)

# Get the form from the response
form = contact_ghn.forms[0]

# Update the form fields with username and password
form.fields['username'] = ghn_creds.GetNetworkCredential().Username
form.fields['password'] = ghn_creds.GetNetworkCredential().Password

# Send a POST request to the URL with the form data and store the response
contact_ghn = session.post(url + form.action, data=form.fields)

# Initialize IP_counter
IP_counter = 0

# Read indexedIPs from the file
with open(f"{working_ticket}/extractedIPs-combined.txt", "r") as file:
    indexedIPs = file.readlines()

# Iterate over indexedIPs
for line in indexedIPs:
    index, ip = line.strip().split(',')
    increment = f"{IP_counter:04d}"
    ipParams = {"ip": ip, "withinSubnet": "true"}

    print(f"Please wait. Requesting detailed information for {ip}...")
    
    # Send a POST request to resolve the IP
    results = session.post(url + '/inventory/resolveIP', data=ipParams).json()

    # Define ghn properties
    ghn_properties = {
        "Index": index,
        "IP": results['ip'],
        "FW_IP": results['subnet'],
        "VLAN": results['vlanName'],
        "Cluster": results['cluster'],
        "Firewall": results['firewall'],
        "Zone": results['zoneName'],
        "App": results['applicationName'],
        "Policy": results['policyName'],
        "Vendor": results['vendor'],
        "Model": results['model'],
        "Version": results['version'],
        "Found": results['found']
    }

    # Write ghn properties to a JSON file
    with open(f"{working_ticket}/ip_info-{increment}.json", "w") as file:
        json.dump(ghn_properties, file)

    # Sleep for 100 milliseconds
    time.sleep(0.1)
