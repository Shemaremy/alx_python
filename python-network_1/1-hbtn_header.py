import requests
import sys

url = sys.argv[1]
resp = requests.get(url)
m = resp.headers.get('X-Request-Id')
print(f"X-Request-Id: {m}" if m else "X-Request-Id not found")
