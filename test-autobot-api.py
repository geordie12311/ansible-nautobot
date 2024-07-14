import requests

# Nautobot API endpoint
url = 'http://192.168.1.21/';

# Nautobot API key
api_key = 'fa00b2c370cf7814805c140ec71ef0c9ce9202de'

# Headers
headers = {
'Accept': 'application/json',
'Authorization': f'Token {api_key}'
}

# Make GET request to Nautobot API
response = requests.get(url, headers=headers)
# Check the response status code
if response.status_code == 200:
    print('API key is valid. Successful connection to Nautobot API.')
else:
    print('API key is invalid. Failed to connect to Nautobot API.')

# Print the response body
print(response.json())

