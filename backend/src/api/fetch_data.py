import requests
from config.settings import API_BASE_URL, API_KEY

def fetch_company_data(company_id):
    params = {
        "id": company_id,
        "api_key": API_KEY
    }

    try:
        response = requests.get(API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data for {company_id}: {e}")
        return None