#Fetching data from the url page provided

import requests    #This package is used for making HTTP requests
url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print(response.text)            #By running this, everything u see in the output pannel is data from such webpage










#