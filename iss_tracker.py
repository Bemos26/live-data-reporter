import requests
import datetime
import os

def track_iss():
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        position = data["iss_position"]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        latitude = position["latitude"]
        longitude = position["longitude"]

        print(f"\n🌍 ISS Current Location at {timestamp}:")
        print(f"   Latitude:  {latitude}")
        print(f"   Longitude: {longitude}")

        # Make sure /data exists
        os.makedirs("data", exist_ok=True)

        with open(os.path.join("data", "iss_data.txt"), "a") as f:
            f.write(f"\n[{timestamp}] ISS Location:\n")
            f.write(f"   Latitude:  {latitude}\n")
            f.write(f"   Longitude: {longitude}\n")

    except requests.RequestException as e:
        print("❌ Error fetching ISS data:", e)