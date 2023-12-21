import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

resp = requests.post(url, data={'email': email})
print(resp.text)
