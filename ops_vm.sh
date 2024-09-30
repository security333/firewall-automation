#!/bin/bash

# Variables (modify these with your actual OpenStack resources)
FLAVOR="m1.medium"
IMAGE="ubuntu-20.04"
KEY_NAME="mykey"
SECURITY_GROUP="default"
VM_NAME="my-vm"
NETWORK_1="network-1-id" # Replace with actual network ID
NETWORK_2="network-2-id" # Replace with actual network ID
NETWORK_3="network-3-id" # Replace with actual network ID
NETWORK_4="network-4-id" # Replace with actual network ID

# Check if required OpenStack environment variables are sourced
if [[ -z "$OS_AUTH_URL" || -z "$OS_PROJECT_NAME" ]]; then
  echo "Please source your OpenStack credentials before running this script."
  exit 1
fi

# Function to create a VM with 4 networks
create_vm() {
  echo "Creating VM: $VM_NAME with 4 networks..."

  openstack server create \
    --flavor "$FLAVOR" \
    --image "$IMAGE" \
    --key-name "$KEY_NAME" \
    --security-group "$SECURITY_GROUP" \
    --nic net-id="$NETWORK_1" \
    --nic net-id="$NETWORK_2" \
    --nic net-id="$NETWORK_3" \
    --nic net-id="$NETWORK_4" \
    "$VM_NAME"

  if [[ $? -eq 0 ]]; then
    echo "VM $VM_NAME created successfully."
  else
    echo "Failed to create VM $VM_NAME."
    exit 1
  fi
}

# Function to allocate and associate a floating IP
allocate_floating_ip() {
  echo "Allocating floating IP..."
  FLOATING_IP=$(openstack floating ip create <external-network-id> -f value -c floating_ip_address)

  if [[ -n "$FLOATING_IP" ]]; then
    echo "Floating IP $FLOATING_IP allocated."

    # Associate the floating IP with the VM
    echo "Associating Floating IP with VM $VM_NAME..."
    openstack server add floating ip "$VM_NAME" "$FLOATING_IP"
    
    if [[ $? -eq 0 ]]; then
      echo "Floating IP $FLOATING_IP associated with VM $VM_NAME."
    else
      echo "Failed to associate Floating IP with VM $VM_NAME."
    fi
  else
    echo "Failed to allocate Floating IP."
  fi
}

# Execute the functions
create_vm
allocate_floating_ip

