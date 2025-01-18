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
