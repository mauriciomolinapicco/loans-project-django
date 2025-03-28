import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://8f7frdw0y5.execute-api.us-east-1.amazonaws.com/prod/validate"

headers = {
    'Content-Type':'application/json',
    'x-api-key':os.getenv("API_KEY")
}

data = {
    'cuil':9360013391
}

res = requests.post(URL, headers=headers, json=data)

print(res.status_code)

response_data = res.json()
approved = response_data['status']
print(approved == 'approved')