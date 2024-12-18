import os
import subprocess

def create_service_file(service_name, script_path, username, groupname):
    """
    Create a systemd service file for the given script.
    """
    service_content = f"""[Unit]
Description={service_name} Service
After=network.target

[Service]
ExecStart={script_path}
Restart=always
User={username}
Group={groupname}

[Install]
WantedBy=multi-user.target
"""
    service_file_path = f"/etc/systemd/system/{service_name}.service"
    with open(service_file_path, 'w') as service_file:
        service_file.write(service_content)
    
    print(f"Service file created at {service_file_path}")
    return service_file_path

def setup_service(service_name, script_path, username, groupname):
    """
    Automates the creation, enabling, and starting of a systemd service.
    """
    # Create the service file
    service_file_path = create_service_file(service_name, script_path, username, groupname)

    # Reload systemd to recognize the new service
    subprocess.run(["systemctl", "daemon-reload"], check=True)

    # Enable and start the service
    subprocess.run(["systemctl", "enable", service_name], check=True)
    subprocess.run(["systemctl", "start", service_name], check=True)

    print(f"Service '{service_name}' has been enabled and started successfully.")

if __name__ == "__main__":
    # Gather user input for service creation
    service_name = input("Enter the name of the service: ").strip()
    script_path = input("Enter the full path to your script (e.g., /usr/local/bin/your_script): ").strip()
    username = input("Enter the username to run the service: ").strip()
    groupname = input("Enter the group name for the service: ").strip()

    # Validate the script path
    if not os.path.exists(script_path):
        print(f"Error: The script path '{script_path}' does not exist.")
    else:
        # Create and setup the service
        setup_service(service_name, script_path, username, groupname)
