# XPEL Installers Scraper

This project is a web scraper that extracts installer information from [XPEL's Installer Locator](https://www.xpel.com/installer-locator) using Playwright.

## Features
- Automatically navigates to the XPEL installer locator page
- Clicks "Load More" until all data is loaded
- Extracts installer details:
  - Name
  - Address
  - Phone number
  - Website
  - Products offered
- Saves the extracted data into:
  - CSV file (`data/xpel_installers_playwright.csv`)
  - Excel file (`data/xpel_installers_playwright.xlsx`)

## Requirements
- Python 3.7+
- Playwright
- openpyxl

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/xpel-installers-scraper.git
   cd xpel-installers-scraper
   ```
2. Install dependencies:
   ```sh
   pip install playwright openpyxl
   ```
3. Install Playwright browsers:
   ```sh
   playwright install
   ```

## Usage
Run the script using:
```sh
python scraper.py
```

## Output
The script will generate two output files:
- `data/xpel_installers_playwright.csv` (CSV format)
- `data/xpel_installers_playwright.xlsx` (Excel format)

## Notes
- The script runs Playwright in non-headless mode (`headless=False`). Change it to `True` if you want to run it in the background.
- If the script fails to load the page within the timeout, it will exit gracefully.

## License
This project is licensed under the MIT License.

## Author
Andre pradika

