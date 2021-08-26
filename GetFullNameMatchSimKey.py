# Get API key at www.interzoid.com/register
import requests

response = requests.get('https://api.interzoid.com/getfullnamematch?license=YOURAPIKEY&fullname=bill johnson')

print(response.text)

if response.status_code == 200:
  data = response.json()
  print(data["SimKey"])
else:
  print("error")
