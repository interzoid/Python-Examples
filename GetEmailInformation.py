# Get API key at www.interzoid.com/register
import requests

response = requests.get('https://api.interzoid.com/getemailinfo?license=YOURAPIKEY&email=winston.smith@maths.ox.ac.uk')

print(response.text)

if response.status_code == 200:
  data = response.json()
  print(data["Info"])
