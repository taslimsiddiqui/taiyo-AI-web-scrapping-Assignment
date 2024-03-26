
Taiyo.ai Data Engineer Task Summary

Hello, I’m Taslim Siddiqui applying for the role of Data Engineer (Web Scraper). I’m a complete novice to this process and even though I tried my best to complete the task with a successful resolution, I could only write the program partially. I’m uploading the program file and summary to the Google Drive and also pushing this code for your evaluation. I have done some research and web surfing about Web Scraping and I’m describing the theoretical aspects of what I understood regarding Web Scraping below in my own words:

# Web Scraping with Selenium and BeautifulSoup

This Python script automates the process of scraping data from a website that lists active tenders. It uses Selenium for web automation and BeautifulSoup for HTML parsing.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium (`pip install selenium`)
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Pillow (`pip install pillow`)

You also need to have Chrome installed on your system and download the appropriate ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the ChromeDriver executable in the same directory as the script.

## Setup

1. Clone the repository or download the script.
2. Install the dependencies mentioned in the prerequisites.
3. Replace the placeholder API key with your actual OCR.space API key in the script.
4. Run the script using `python script_name.py`.

## Script Overview

- The script navigates to the webpage listing the active tenders.
- It handles CAPTCHA challenges using OCR (Optical Character Recognition) with the help of the OCR.space API.
- Once the CAPTCHA is solved, it scrapes the tender data from the table on the page.
- It navigates through multiple pages of tenders, if available, and continues scraping.
- Finally, it saves the scraped data to a CSV file named `tender.csv`.

## Important Notes

- Make sure to use a valid OCR.space API key for CAPTCHA solving.
- This script assumes a specific structure of the webpage. Any changes to the webpage structure may require modifications to the script.
- Be mindful of web scraping ethics and legal considerations. Respect the website's terms of service and avoid making too many requests in a short period to prevent IP blocking.

Feel free to modify the script as needed for your specific use case.
