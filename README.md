Live Data Reporter
A terminal-based dashboard for fetching real-time astronaut data, ISS location, stock prices, and business headlines.

📁 Features
- 🔭 View which astronauts are currently in space
- 🌍 Track the real-time location of the ISS
- 📰 Fetch top U.S. business news or current IBM stock prices
- 💾 Auto-logs data in a local file for future reference

🚀 How to Run
- Clone the repository
git clone https://github.com/Bemos26/live-data-reporter.git
cd live-data-reporter


- Create and activate a virtual environment
python -m venv venv
# Then:
# On Windows CMD
venv\Scripts\activate.bat
# On PowerShell
.\venv\Scripts\Activate.ps1


- Install the required packages
pip install -r requirements.txt


- Add your API keys
Create a .env file and add:
NEWS_API_KEY=your_newsapi_key
STOCK_API_KEY=your_alphavantage_key


- Run the app
python main.py



🗃️ Folder Structure
live-data-reporter/
│
├── main.py                  # CLI menu logic
├── astronauts.py            # Astronaut data module
├── iss_tracker.py           # ISS location tracker
├── news_or_stock.py         # Stock/news fetcher
├── .env                     # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── data/
    └── iss_data.txt         # Saved reports



🛡️ Notes
- Never push .env files to GitHub
- API rate limits apply (especially for NewsAPI and Alpha Vantage free plans)
- Built by Benson, with support from Copilot ☄️
