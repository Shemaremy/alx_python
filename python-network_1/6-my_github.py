import requests
import sys

username = sys.argv[1]
access_token = sys.argv[2]
url = "https://api.github.com/user"
auth = (username, access_token)

resp = requests.get(url, auth=auth)

if resp.status_code == 200:
    udata = resp.json()
    uid = udata.get('id', '')
    print(f"{uid}" if uid else "Unable")

else:
    print("None")

