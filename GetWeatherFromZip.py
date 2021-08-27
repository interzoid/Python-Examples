# Get API key at www.interzoid.com/register
import requests

response = requests.get('https://api.interzoid.com/getweatherzipcode?license=YOURAPIKEY&zip=94111')

print(response.text)

if response.status_code == 200:
  data = response.json()
  print(data["TempF"])
