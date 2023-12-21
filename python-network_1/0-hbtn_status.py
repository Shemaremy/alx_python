'''
The program below will be fetching
the given url by only using
package requests

Means that it will retreive all information from the url provided here
instead of going to browser seatchbar and searching
'''
import requests    #This package is used for making HTTP requests
url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print(f"Body response:\n\t- type: {type(response.text)}\n\t- content: {response.text}")