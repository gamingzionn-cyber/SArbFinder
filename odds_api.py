import os
import requests

API_KEY = os.getenv("ODDSSHOPPER_API_KEY")
BASE_URL = "https://api.oddsshopper.com/v1/odds"

def get_live_odds(sport="soccer"):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"sport": sport}
    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data["odds"]  # adjust based on actual API structure
