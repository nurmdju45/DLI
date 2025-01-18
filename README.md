# DLI Web Scraper

This repository contains a Python script for scraping DLI (Daily Light Integral) data from the website [suntrackertech.com](https://dli.suntrackertech.com/), using Selenium WebDriver. The script retrieves data for multiple latitude-longitude coordinates and stores the results in a CSV file for further analysis.

## Features

- Extract DLI data for specific latitude and longitude values.
- Scrape data for all months (Jan-Dec) from the website.
- Save the results in a CSV file.
- Fully automated web scraping using Selenium.

## Prerequisites

To run the script, make sure you have the following installed:

- **Python 3.x**
- **Selenium**: WebDriver for automating web browser interaction.
- **ChromeDriver**: Compatible version of the Chrome browser driver for Selenium.
- **CSV**: Used for reading and writing CSV files.

You can install the necessary libraries using `pip`:

```bash
pip install selenium
```
Note: Ensure the Chrome WebDriver is installed and available in your system's PATH.

## Files

- `bang_b.csv`: A CSV file containing latitude and longitude values for the locations for which you want to scrape data.
- `DLI_results.csv`: The output CSV file containing each location's DLI data.

## How It Works

- **Input CSV File**: The script reads a CSV file (e.g., `bang_b.csv`) containing a list of latitude-longitude pairs (one per row).
  
- **Selenium Interaction**: For each latitude-longitude pair, the script opens the web page and fills out the input field with the corresponding latitude and longitude.

- **Extracting Data**: After submitting the data, the script extracts the DLI values from the page. These values correspond to each month of the year (Jan-Dec).

- **Saving Results**: The script appends the scraped DLI values for each location to an output CSV file (`DLI_results.csv`).

- **Repeat for Each Entry**: This process repeats for each entry in the input CSV file.

## Usage

### Clone the Repository:

```bash
git clone https://github.com/yourusername/DLI.git
```
## Prepare the Input CSV File

Prepare the input CSV file (bang_b.csv) with latitude and longitude values. The file should have the following format:
```csv
Latitude,Longitude
23.8103,90.4125
22.3636,91.1560
```




