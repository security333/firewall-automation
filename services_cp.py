import subprocess

def create_service(service_name, service_file):
    # Copy service file
    subprocess.run(["cp", service_file, f"/etc/systemd/system/{service_name}.service"], check=True)
    
    # Reload systemd, enable, and start the service
    subprocess.run(["systemctl", "daemon-reload"], check=True)
    subprocess.run(["systemctl", "enable", service_name], check=True)
    subprocess.run(["systemctl", "start", service_name], check=True)

    print(f"Service {service_name} created, enabled, and started successfully.")

if __name__ == "__main__":
    service_name = input("Enter the service name: ")
    service_file = input("Enter the path to the service file: ")
    create_service(service_name, service_file)
