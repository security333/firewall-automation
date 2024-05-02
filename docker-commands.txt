Managing Containers:
Start a container:
docker start <container_name_or_id>

Stop a container:
docker stop <container_name_or_id>

Restart a container:
docker restart <container_name_or_id>

Remove a container:
docker rm <container_name_or_id>

List running containers:
docker ps

List all containers (including stopped ones):
docker ps -a

Inspect a container:
docker inspect <container_name_or_id>

Managing Images:
Pull an image from Docker Hub:
docker pull <image_name>

List local images:
docker images

Remove an image:
docker rmi <image_name_or_id>

Running Containers:
Run a container from an image:
docker run <image_name>

Run a container in the background (detached mode):
docker run -d <image_name>

Run a container with a specific name:
docker run --name <container_name> <image_name>

Run a container and map ports:
docker run -p <host_port>:<container_port> <image_name>

Run a container with environment variables:
docker run -e <key=value> <image_name>

Docker Network:
List networks:
docker network ls

Inspect a network:
docker network inspect <network_name_or_id>

Docker Volumes:
List volumes:
docker volume ls

Inspect a volume:
docker volume inspect <volume_name_or_id>

Remove a volume:
docker volume rm <volume_name_or_id>

Docker Compose:
Run services defined in a Compose file:
docker-compose up

Stop services:
docker-compose down

Build or rebuild services:
docker-compose build

List services:
docker-compose ps
