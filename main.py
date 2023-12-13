#From Open Weather API
from keys import *

import requests

response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={my_lat}&lon={my_long}&appid={api_key}')
status = response.status_code
data = response.json()
print(f"Status code: {status}")
print(data)