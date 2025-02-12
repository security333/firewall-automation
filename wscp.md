Step 1: Download and Install WinSCP
Download WinSCP:

Visit the WinSCP download page.
Click the download link for the latest version.
Install WinSCP:

Run the downloaded installer.
Follow the installation prompts. You can choose the default installation options for a typical setup.
Launch WinSCP after installation is complete.
Step 2: Launch WinSCP and Set Up a New Session
Open WinSCP:

When you launch WinSCP, you’ll see the “Login” window.
Enter Connection Details:

File Protocol:
Choose SFTP (recommended) or SCP from the dropdown. SFTP is most common for Linux servers.
Host Name:
Enter the IP address or domain name of your Linux server.
Port Number:
The default for SFTP/SSH is 22. Change it only if your server uses a different port.
User Name:
Enter your Linux server username.
Password:
Enter your password. (If you use key-based authentication, see the “Advanced Options” below.)
Optional – Save the Session:
You can click “Save…” to store these settings for future use.
Advanced Options (for Key-Based Authentication):

Click Advanced… in the Login window.
Navigate to SSH > Authentication.
Under “Private key file,” browse to select your private key file (e.g., a .ppk file if using PuTTYgen to convert an OpenSSH key).
Click OK to return to the main Login window.
Step 3: Connect to the Linux Server
Start the Connection:

Click the Login button.
Host Key Verification:

The first time you connect, a dialog may appear asking if you trust the server’s host key.
Verify the key fingerprint with your system administrator if possible.
Click Yes or Accept to proceed.
Successful Connection:

Once connected, WinSCP will display a dual-pane interface:
The left pane shows your local files.
The right pane shows files on the remote Linux server.
Step 4: Navigating and Transferring Files
Browsing Files:

Use the panes to navigate through directories on your local machine (left) and the remote server (right).
Transferring Files:

Drag and Drop:
Simply drag files from one pane to the other to copy them.
Right-Click Options:
Right-click on a file or folder and select options like Upload, Download, or Edit.
Transfer Settings:
You can click on the gear icon or go to Options > Preferences > Transfers to adjust settings like transfer mode (binary/text) and speed limits.
Step 5: Ending Your Session
Disconnect:

When finished, you can close the WinSCP window or go to Session > Disconnect from the menu.
This will safely terminate the connection to the Linux server.
Closing WinSCP:

After disconnecting, you can close the application.
