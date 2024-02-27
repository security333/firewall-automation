import json
import os

working_ticket = "your_working_ticket_directory_path"  # Specify your working ticket directory path
ticket = "your_ticket_name"  # Specify your ticket name

# Combine JSON files into a single JSON file
with open(os.path.join(working_ticket, f"{ticket}-combined.json"), "a") as combined_file:
    combined_file.write("{\n\"results\": [\n")

    # Append contents of individual JSON files
    for filename in os.listdir(working_ticket):
        if filename.startswith("ip_info-") and filename.endswith(".json"):
            with open(os.path.join(working_ticket, filename), "r") as json_file:
                combined_file.write(json_file.read().rstrip("\n") + ",\n")

    # End the JSON array
    combined_file.write("]\n}")

# Read combined JSON file and extract required fields
with open(os.path.join(working_ticket, f"{ticket}-combined.json"), "r") as combined_file:
    combined_data = json.load(combined_file)
    results = combined_data["results"]
    extracted_data = [{field: item[field] for field in ["Index", "IP", "FW_IP", "VLAN", "Cluster", "Firewall", "Zone", "App", "Policy", "Vendor", "Model", "Version", "Found"]} for item in results]

# Write extracted data to CSV file
with open(os.path.join(working_ticket, f"{ticket}-info.csv"), "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["Index", "IP", "FW_IP", "VLAN", "Cluster", "Firewall", "Zone", "App", "Policy", "Vendor", "Model", "Version", "Found"])
    writer.writeheader()
    writer.writerows(extracted_data)

# Remove temporary files
for filename in os.listdir(working_ticket):
    if filename.endswith((".txt", ".json")):
        os.remove(os.path.join(working_ticket, filename))

# Open the CSV file
os.system(f"start {os.path.join(working_ticket, f'{ticket}-info.csv')}")

print(f"Complete! The information you requested can be found at {os.path.join(working_ticket, f'{ticket}-info.csv')}")
