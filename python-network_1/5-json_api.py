import requests
import sys

url = "http://0.0.0.0:5000/search_user"
q = sys.argv[1] if len(sys.argv) > 1 else ""
resp = requests.post(url, data={'q': q})

try:
    js = resp.json()
    if js:
        uid = js.get('id', '')
        uname = js.get('name', '')
        print(f"[{uid}]{uname}" if uid and uname else "No result")
    
    else:
        print("No result")

except ValueError:
    print("Not a valid JSON")