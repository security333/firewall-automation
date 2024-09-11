import openstack

# Initialize and connect to OpenStack
conn = openstack.connect(cloud='your_openstack_cloud_name')

# Parameters
vm_count = 10
image_name = "ubuntu-20.04"  # Example image
flavor_name = "m1.small"     # Example flavor
network_1_name = "network_1" # First network name
network_2_name = "network_2" # Second network name
keypair_name = "your_keypair_name"
security_group_name = "default"

# Get the resources
image = conn.compute.find_image(image_name)
flavor = conn.compute.find_flavor(flavor_name)
network_1 = conn.network.find_network(network_1_name)
network_2 = conn.network.find_network(network_2_name)
security_group = conn.network.find_security_group(security_group_name)
keypair = conn.compute.find_keypair(keypair_name)

# Create VMs with multiple network interfaces (multihomed)
for i in range(vm_count):
    vm_name = f"multihomed-vm-{i+1}"

    # Define networks (multihoming)
    networks = [
        {"uuid": network_1.id},  # Interface on network 1
        {"uuid": network_2.id},  # Interface on network 2
    ]

    # Create the VM
    server = conn.compute.create_server(
        name=vm_name,
        image_id=image.id,
        flavor_id=flavor.id,
        networks=networks,
        key_name=keypair.name,
        security_groups=[security_group.name]
    )

    # Wait for the server to be fully provisioned
    server = conn.compute.wait_for_server(server)

    print(f"Created and deployed multihomed VM: {vm_name}")

print(f"{vm_count} multihomed VMs created successfully.")
