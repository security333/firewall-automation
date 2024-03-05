from netmiko import ConnectHandler
import getpass

def ssh_connect(username, password, hostname, device_type='cisco_ios'):
    try:
        # Define device parameters
        device = {
            'device_type': device_type,
            'host': hostname,
            'username': username,
            'password': password,
        }

        # Establish SSH connection
        ssh_session = ConnectHandler(**device)
        print("Successfully connected to the server.")

        # Keep the connection open
        # You can perform any operations here

    except Exception as e:
        print("Error:", e)
        ssh_session.disconnect()

def main():
    # Get user input for SSH connection
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")
    hostname = input("Enter the hostname or IP address of the server: ")

    # Call the function to establish SSH connection
    ssh_connect(username, password, hostname)

if __name__ == "__main__":
    main()
