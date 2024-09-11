import openstack

# Initialize and authenticate with the OpenStack cloud
conn = openstack.connect(cloud='your_cloud_name')

# Define the network names
networks = ['net1', 'net2']

# Define the flavor and image
flavor_name = 'm1.small'
image_name = 'ubuntu-20.04'

# Find the flavor and image
flavor = conn.compute.find_flavor(flavor_name)
image = conn.compute.find_image(image_name)

# Create and deploy 10 VMs
for i in range(10):
    # Create a server with multiple networks
    server = conn.compute.create_server(
        name=f'multihomed-vm-{i}',
        image_id=image.id,
        flavor_id=flavor.id,
        networks=[{"uuid": conn.network.find_network(net).id} for net in networks]
    )
    # Wait for the server to be active
    server = conn.compute.wait_for_server(server)
    print(f'Server {server.name} created and active.')

print('All VMs have been created and deployed.')
