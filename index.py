import requests
import json

url = 'https://nstest.com'
session = requests.Session()
contact_nsd = session.get(url)
form = contact_nsd.forms[0]
form.fields['username'] = nsd_creds.GetNetworkCredentail().Username
form.fields['password'] = nsd_creds.GetNetworkCredentail().Password
contact_nsd = session.post(url + form.action, data=form.fields)
ip_counter = 0

indexed_ips = open('extractedIPs-combined.txt').readlines()
for line in indexed_ips:
    line = line.strip().split(',')
    index = line[0]
    ip = line[1]
    ip_params = {'ip': ip, 'withinSubnet': 'true'}
    print(f"Please wait. Requesting detailed information for {ip}...")
    results = session.post(url + '/inventory/resolveIP', data=ip_params)
    nsd_properties = {
        'Index': index,
        'IP': results.json()['ip'],
        'FW_IP': results.json()['subnet'],
        'VLAN': results.json()['vlanName'],
        'Cluster': results.json()['cluster'],
        'Firewall': results.json()['firewall'],
        'Zone': results.json()['zoneName'],
        'App': results.json()['applicationName'],
        'Policy': results.json()['policyName'],
        'Vendor': results.json()['vendor'],
        'Model': results.json()['model'],
        'Version': results.json()['version'],
        'Found': results.json()['found']
    }
    with open(f"ip_info-{ip_counter:04d}.json", "w") as file:
        json.dump(nsd_properties, file)
    time.sleep(0.1)
