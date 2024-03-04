import paramiko

def ssh_connect(username, password, hostname, port=22):
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh_client.connect(hostname, port, username, password)
        print("Successfully connected to the server.")

        # Perform any SSH commands or operations here
        # For example, execute a command on the server
        stdin, stdout, stderr = ssh_client.exec_command("ls -l")
        print("Output of 'ls -l' command:")
        for line in stdout:
            print(line.strip())

        # Close the SSH connection
        ssh_client.close()
    except Exception as e:
        print("Error:", e)

def main():
    # Get user input for SSH connection
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hostname = input("Enter the hostname or IP address of the server: ")

    # Call the function to establish SSH connection
    ssh_connect(username, password, hostname)

if __name__ == "__main__":
    main()
