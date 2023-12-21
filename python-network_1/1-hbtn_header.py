import requests
import sys

url = sys.argv[1]
resp = requests.get(url)
m = resp.headers.get('X-Request-Id')
print(f"{m}" if m else "None")
