import requests  # Lets us make HTTP requests
import datetime  # For timestamping data
import os        # For working with file paths and directories


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"  # API endpoint
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses

        data = response.json()  # Parse the response as JSON
        people = data.get("people", [])
        total = data.get("number", 0)

        print(f"\n 🧑‍🚀 There are {total} astronauts in space:\n")
        for person in people:
            print(f" - {person['name']} aboard {person['craft']}")

               # Save report to file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_dir = os.path.join("data")
        os.makedirs(data_dir, exist_ok=True)  # 🔧 This creates 'data/' if it doesn't exist

        file_path = os.path.join(data_dir, "iss_data.txt")
        with open(file_path, "a") as f:
            f.write(f"\n[{timestamp}] {total} astronauts in space:\n")
            for person in people:
                f.write(f" - {person['name']} aboard {person['craft']}\n")
    except requests.RequestException as e:
        print("❌ Error fetching astronaut data:", e)