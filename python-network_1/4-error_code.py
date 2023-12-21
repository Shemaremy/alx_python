import requests
import sys

url = sys.argv[1]

try:
    resp = requests.get(url)
    print(resp.text)

    if resp.status_code >= 400:
     print(f"Error code:{resp.status_code}")

except requests.RequestException as e:
    print(f"Error: {e}")
