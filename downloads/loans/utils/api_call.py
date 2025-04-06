import requests
import os
from dotenv import load_dotenv
load_dotenv()

URL = "https://8f7frdw0y5.execute-api.us-east-1.amazonaws.com/prod/validate"

def make_api_call(cuil):
    headers = {
        'Content-Type':'application/json',
        'x-api-key':os.getenv('API_KEY')
    }

    data = {
        'cuil':cuil
    }

    res = requests.post(URL, headers=headers, json=data)

    if res.status_code == 200:
        response_data = res.json()
        approved = response_data['status']
        print(approved)
        print(res.text)
        return (approved == 'approved')
    
    return False