'''
The program below will be fetching
the given url by only using
package requests
'''
import requests
url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print(f"Body response:\n\t    - type: {type(response.text)}\n\t    - content: {response.text}")