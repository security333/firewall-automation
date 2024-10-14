#!/bin/bash

# Get the list of running containers
containers=$(docker ps -q)

# Check if there are any running containers
if [ -z "$containers" ]; then
  echo "No running containers found."
  exit 0
fi

# Loop through each container
for container in $containers; do
  # Get the container name
  container_name=$(docker inspect --format '{{.Name}}' "$container" | sed 's/^\/\([^.]*\).*/\1/')
  
  # Ask user if they want to delete the container
  read -p "Do you want to delete the container $container_name (ID: $container)? (y/n): " response
  
  if [[ "$response" == "y" || "$response" == "Y" ]]; then
    echo "Stopping container: $container_name"
    docker stop "$container"
    echo "Deleting container: $container_name"
    docker rm "$container"
  else
    echo "Skipping container: $container_name"
  fi
done

echo "All specified containers have been processed."
