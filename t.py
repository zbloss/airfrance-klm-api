import os

import requests
from dotenv import load_dotenv

load_dotenv()

AF_KLM_API_KEY = os.getenv("AF_KLM_API_KEY")
AF_KLM_API_SECRET = os.getenv("AF_KLM_API_SECRET")

headers = {"API-Key": AF_KLM_API_KEY, "Content-Type": "application/json"}

response = requests.get(
    "https://api.airfranceklm.com/opendata/flightstatus", headers=headers
)
print(response.status_code)

print(response.json())