import os

# All apps in list
programs = {
    "1": ("Flask Server", "modules/01_flask_server.py"),
    "2": ("Get Website Title", "modules/02_get_website_title.py"),
    "3": ("QR Code Generator", "modules/03_qrcode_generator.py"),
    "4": ("Save HTML Webpage", "modules/04_save_webpage.py"),
    "5": ("Translator", "modules/05_translator.py"),
    "6": ("Quick Plot", "modules/06_quick_plot.py"),
    "7": ("Create Zip", "modules/07_create_zip.py"),
    "8": ("Github Repo Info", "modules/08_github_repo_info.py"),
    "9": ("Language Detector", "modules/09_language_detector.py"),
    "10": ("Weather Forecast", "modules/10_weather_forecast.py"),
}

# This function only show all programs
def menu():
    print("\n=== One Line Challenge Menu ===")
    for key, (name, _) in programs.items():
        print(f"[{key}] {name}")
    print("[0] Quit")
        
# This function run the selected option
def main():
    while True:
        menu()
        select = input("Select one option: ").strip()
        # Conditionals
        if select == "0":
            print("Bye...")
            break
        elif select in programs:
            name, path = programs[select]
            print(f"\nRunning: {name}\n")
            os.system(f"python {path}")
        else:
            print("Invalid option, try again!")
        
if __name__ == "__main__":
    main()