import requests
import json

indexedIPs = [("1", "192.168.1.1"), ("2", "192.168.1.2"), ("3", "192.168.1.3")]  # Example list of indexed IPs
url = "your_api_url"  # Specify the API URL
mysession = requests.Session()  # Create a session

for index, ip in indexedIPs:
    increment = '{:04d}'.format(index)
    ip_params = {"ip": ip, "withinSubnet": "true"}
    
    print(f"Please wait. Requesting detailed information for {ip}...")
    response = mysession.post(url + '/inventory/resolveIP', json=ip_params)
    results = response.json()

    NSD_properties = {
        "Index": index,
        "IP": results["ip"],
        "FW_IP": results["subnet"],
        "VLAN": results["vlanName"],
        "Cluster": results["cluster"],
        "Firewall": results["firewall"],
        "Zone": results["zoneName"],
        "App": results["applicationName"],
        "Policy": results["policyName"],
        "Vendor": results["vendor"],
        "Model": results["model"],
        "Version": results["version"],
        "Found": results["found"]
    }

    with open(f"ip_info-{increment}.json", "w") as json_file:
        json.dump(NSD_properties, json_file)

    # Delay for 100 milliseconds
    import time
    time.sleep(0.1)
