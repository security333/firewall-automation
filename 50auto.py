import yaml
import os

def load_cloud_init(file_path):
    """Load the cloud-init YAML file."""
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return None

    with open(file_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error loading YAML: {e}")
            return None

def save_cloud_init(file_path, data):
    """Save the updated cloud-init YAML file."""
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"Updated configuration saved to {file_path}.")

def get_interface_by_selection(selection):
    """Map numeric selection to interfaces."""
    mapping = {
        "1": "ens4",  # EDN
        "2": "ens5",  # RAN
        "3": "ens6",  # WSN
    }
    return mapping.get(selection)

def get_gateway_from_routes(routes):
    """Get the gateway ('via') from existing routes."""
    if routes:
        return routes[0].get("via")  # Assumes the first route contains the gateway
    return None

def network_exists(interface_config, network):
    """Check if the network already exists in the interface configuration."""
    if "addresses" in interface_config and network in interface_config["addresses"]:
        return True
    if "routes" in interface_config:
        for route in interface_config["routes"]:
            if route.get("to") == network:
                return True
    return False

def add_network_to_interface(config, interface, network):
    """Add the network to the specified interface in the config."""
    if interface not in config.get("network", {}).get("ethernets", {}):
        print(f"Interface {interface} not found in configuration.")
        return config

    iface_config = config["network"]["ethernets"][interface]

    # Ensure the network doesn't already exist
    if network_exists(iface_config, network):
        print(f"Network {network} already exists on interface {interface}.")
        return config

    # Get the gateway from the existing routes
    gateway = get_gateway_from_routes(iface_config.get("routes", []))
    if not gateway:
        print(f"No existing gateway found for interface {interface}. Cannot add network.")
        return config

    # Add the new network to addresses and routes
    iface_config.setdefault("addresses", []).append(network)
    iface_config.setdefault("routes", []).append({
        "to": network,
        "via": gateway
    })
    print(f"Added network {network} to interface {interface} with gateway {gateway}.")
    return config

def main():
    file_path = "50-cloud-init.yaml"
    config = load_cloud_init(file_path)
    if not config:
        return

    # Display network type options
    print("Select network type:")
    print("1: EDN")
    print("2: RAN")
    print("3: WSN")
    network_selection = input("Enter your choice (1, 2, or 3): ").strip()

    # Get the interface based on the user's selection
    interface = get_interface_by_selection(network_selection)
    if not interface:
        print("Invalid selection. Please enter 1, 2, or 3.")
        return

    # Ask the user for the network address
    network = input("Enter network address (e.g., 10.2.4.5/22): ").strip()

    # Update the configuration
    updated_config = add_network_to_interface(config, interface, network)

    # Save the updated configuration
    save_cloud_init(file_path, updated_config)

if __name__ == "__main__":
    main()
