# Get API key at www.interzoid.com/register
import requests

response = requests.get('https://api.interzoid.com/globalpageload?license=YOURAPIKEY&origin=Singapore&url=http://www.ebay.com')

print(response.text)

if response.status_code == 200:
  data = response.json()
  print(data["Seconds"])
