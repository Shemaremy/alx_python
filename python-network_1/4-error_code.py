import requests
import sys

url = sys.argv[1]
resp = requests.get(url)
print(resp.text)

if resp >= 400:
    print(f"Error code:{resp.status_code}")
