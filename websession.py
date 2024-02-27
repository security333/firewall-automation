import requests

# Define the URL
url = 'https://mysite.com'

# Create a session
session = requests.Session()

# Send a GET request to the URL to establish the session
contact_nsd = session.get(url)

# Get the first form from the response
form = contact_nsd.forms[0]

# Set the username and password fields in the form
form.fields['username'] = nsd_creds.username
form.fields['password'] = nsd_creds.password

# Send a POST request with the form data
contact_nsd = session.post(url + form.action, data=form.fields)

# Set the IP counter to 0
IP_counter = 0
