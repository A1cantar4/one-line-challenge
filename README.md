<div align="center">
  <picture>
    <img src="img/logo.png" alt="Logo" width="80%">
  </picture>
</div>

<div align="center">
  <h1>One Line Challenge Python Projects</h1>
</div>

A collection of **10 Simple Python Projects**, each written in **just one line of code**, to demonstrate the language’s power, elegance, and versatility. These challenges illustrate how tasks that would typically require multiple lines can be condensed into concise, functional one-liners without sacrificing clarity or functionality.

---

## Features

Each file inside the `modules/` folder is a **different project**:

- [x] **01_flask_server.py** — Minimal web server using Flask.
- [x] **02_get_website_title.py** — Fetches the `<title>` of any website.
- [x] **03_qrcode_generator.py** — Generates a QR Code from a link or text.
- [x] **04_save_webpage.py** — Saves the HTML content of a webpage locally.
- [x] **05_translator.py** — Translates text into English using Google Translate API.
- [x] **06_quick_plot.py** — Generates and saves a simple chart using matplotlib.
- [x] **07_create_zip.py** — Compresses files into a ZIP archive.
- [x] **08_github_repo_info.py** — Retrieves public repository info from GitHub API.
- [x] **09_language_detector.py** — Detects the language of a given text.
- [x] **10_weather_forecast.py** — Displays the current weather using the free `wttr.in` API.

---

## Project Structure

```
one-line-challenge/
│
├── modules/
│   ├── 01_flask_server.py
│   ├── 02_get_website_title.py
│   ├── 03_qrcode_generator.py
│   ├── 04_save_webpage.py
│   ├── 05_translator.py
│   ├── 06_quick_plot.py
│   ├── 07_create_zip.py
│   ├── 08_github_repo_info.py
│   ├── 09_language_detector.py
│   └── 10_weather_forecast.py
│
├── CHANGELOG.md
├── .gitignore
├── requirements.txt
├── LICENSE
├── README.md
└── assets/
    └── logo.png
```

---

## Requirements.txt

```txt
flask
requests
qrcode
googletrans==4.0.0-rc1
matplotlib
langdetect
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/A1cantar4/one-line-challenge
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- **Linux/macOS**:
```bash
source venv/bin/activate
```
- **Windows**:
```bash
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## How to run

1. Open the `app.py` or run in terminal:
```bash
python app.py
```

2. Select in menu:
```bash
=== One Line Challenge Menu ===
[1] Flask Server
[2] Get Website Title
[3] QR Code Generator
[4] Save HTML Webpage
[5] Translator
[6] Quick Plot
[7] Create Zip
[8] Github Repo Info
[9] Language Detector
[10] Weather Forecast
[0] Quit
Select one option: 
```

3. Enjoy the App!

---

## Contributing

Contributions are welcome!
1. Fork the project
2. Create a branch (`git checkout -b my-feature`)
3. Commit your changes (`git commit -m 'feat: add new feature'`)
4. Push to your branch (`git push origin my-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for more details.

--- 

## Author

**Lucas Alcântara**  
GitHub: [@A1cantar4](https://github.com/A1cantar4)
