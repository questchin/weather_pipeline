import requests as req

from src.config import BASE_URL, API_VERSION, FORECAST_ENDPOINT, LATITUDE, LONGITUDE

def get_data_from_URL():
    url = f"{BASE_URL}/{API_VERSION}/{FORECAST_ENDPOINT}?latitude={LATITUDE}&longitude={LONGITUDE}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    print(f"Getting data from:{url}")
    print("\n")

    try:
        r = req.get(url, timeout=10)
        r.raise_for_status()

    except req.exceptions.RequestException as e:
        print("Something went wrong. Pipeline extraction failed:")
        print(f"{e}")
        
        return None

    else:
        print("Data retrieved successfully.")
        return r.json()
