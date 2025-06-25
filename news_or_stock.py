import requests
import datetime
import os
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

def get_ibm_stock():
    api_key = os.getenv("STOCK_API_KEY")
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={api_key}"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        quote = data.get("Global Quote", {})
        price = quote.get("05. price", "N/A")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n📈 IBM Stock Price at {timestamp}: ${price}")

        os.makedirs("data", exist_ok=True)
        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n[{timestamp}] IBM Stock Price: ${price}\n")

    except requests.RequestException as e:
        print("❌ Error fetching stock data:", e)


def get_business_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={api_key}"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        articles = data.get("articles", [])[:3]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n📰 Top 3 US Business Headlines at {timestamp}:")
        os.makedirs("data", exist_ok=True)
        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n[{timestamp}] US Business News:\n")
            for article in articles:
                title = article.get("title", "No title")
                print(f" - {title}")
                f.write(f" - {title}\n")

    except requests.RequestException as e:
        print("❌ Error fetching business news:", e)


def fetch_choice():
    print("\n📊 What would you like to see?")
    print("1. IBM stock price")
    print("2. US business headlines")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        get_ibm_stock()
    elif choice == "2":
        get_business_news()
    else:
        print("⚠️ Invalid choice.")