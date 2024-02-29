import requests
from bs4 import BeautifulSoup

url = 'https://mysite.com'
session = requests.Session()
contact_nsd = session.get(url)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(contact_nsd.content, 'html.parser')

# Find all form elements
forms = soup.find_all('form')

# Assuming there's at least one form
if forms:
    # Select the first form
    form = forms[0]
    
    # Extract form action URL
    action = form.get('action')
    
    # Extract form fields
    fields = {}
    for input_tag in form.find_all('input'):
        fields[input_tag.get('name')] = input_tag.get('value', '')
    
    # Populate form fields with credentials
    fields['username'] = nsd_creds.username
    fields['password'] = nsd_creds.password
    
    # Perform POST request with form data
    contact_nsd = session.post(url + action, data=fields)

    # Continue processing the response as needed
else:
    print("No forms found on the page")
