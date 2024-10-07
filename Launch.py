import docker
import subprocess

def get_ticket_number():
    # Get the ticket number from the user
    ticket_number = input("Enter the ticket number: ")
    return ticket_number

def create_container(ticket_number):
    # Initialize Docker client
    client = docker.from_env()

    # Define the image and container configuration
    container_image = 'pathfinder_image'  # Replace with your actual Docker image name
    container_name = 'pathfinder_container'

    # Run the container with the ticket number passed as an environment variable
    try:
        container = client.containers.run(
            container_image,
            name=container_name,
            environment={"TICKET_NUMBER": ticket_number},
            detach=True,
            ports={'80/tcp': 8080}  # Adjust the port mapping as necessary
        )
        print(f"Container {container_name} launched successfully with ticket number {ticket_number}.")
        return container
    except docker.errors.ContainerError as e:
        print(f"Error starting container: {e}")
        return None

def run_pathfinder():
    # Example command to start your hosted app Pathfinder inside the container
    # This could also be a subprocess call to run within the container
    try:
        print("Launching Pathfinder app...")
        subprocess.run(["docker", "exec", "pathfinder_container", "python3", "/app/pathfinder.py"])
        print("Pathfinder app is running.")
    except Exception as e:
        print(f"Failed to launch Pathfinder: {e}")

if __name__ == "__main__":
    ticket_number = get_ticket_number()
    container = create_container(ticket_number)

    if container:
        run_pathfinder()

######################################################
'''
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
pip install docker
'''
