import sys
from news_or_stock import fetch_choice
from astronauts import get_astronauts
from iss_tracker import track_iss
def show_menu():
    # This function prints the options your app offers.
    print("\n=== 🚀 Live Data Reporter ===")  # Adds a title/header for the menu
    print("1. View current astronauts")       # Option 1: User wants astronaut data
    print("2. Track ISS location")            # Option 2: User wants ISS coordinates
    print("3. Get IBM stock price or US business headlines")  # Option 3: user chooses between two data types
    print("4. Exit")                          # Option 4: user can close the app

def main():
        while True:
            show_menu()
            choice = input ("Please enter your choice (1-4):").strip()
            if choice == "1":
                print ("Fetching astronaut data...")
                get_astronauts()
            elif choice == "2":
                  print("🛰️ Tracking ISS location...")
                  track_iss()
            elif choice == "3":
                print("📰 Retrieving IBM stock or business news...")
                fetch_choice()
            elif choice == "4":
                print("👋 Exiting... Stay curious, Benson.")
                sys.exit()  # Exits the program cleanly
            else:
                print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
        main()