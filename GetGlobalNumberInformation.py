# Get API key at www.interzoid.com/register-api-account
import requests

response = requests.get('https://api.interzoid.com/getglobalnumberinfo?license=YOURAPIKEY&intlnumber=+4906979550')

print(response.text)

if response.status_code == 200:
  data = response.json()
  print(data["Country"])
