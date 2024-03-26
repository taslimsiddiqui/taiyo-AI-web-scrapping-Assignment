# taiyo-AI-web-scrapping-Assignment
Taiyo.ai Data Engineer Task Summary

Hello, I’m Taslim Siddiqui applying for the role of Data Engineer (Web Scraper). I’m a complete novice to this process and even though I tried my best to complete the task with a successful resolution,
I could only write the program partially. I’m uploading the program file and summary to the Google Drive and also pushing this code for your evaluation. 
I have done some research and web surfing about Web Scraping and I’m describing the theoretical aspects of what I understood regarding Web Scraping below in my own words:
#1 HAVING THE REQUIRED LIBRARIES AND TOOLS IMPORTED

#pip install requests beautifulsoup4 pandas time

from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import time

#2 CREATING A CLASS TO PERFORM SCRAPING AND EXTRACTING DATA
#def extract_data:
page_url = "https://etenders.gov.in/eprocure/app" #url of the page to be scraped
response = requests.get(page_url) #sending HTTP GET request to the website
soup = BeautifulSoup(response.content, 'html.parser') # Parse the HTML code using BeautifulSoup
response = requests.get(page_url)

html_bytes = page_url.read()
html = html_bytes.decode("utf-8")

# Extract the relevant information from the HTML code
tenders = []
tender.append([Tender Title, Reference No, Closing Date, Bid Opening Date])

# Storing the information in a pandas dataframe and converting to CSV format
#def Save_as_CSV:
data_frame = pd.DataFrame(tenders, columns=['Tender Title', 'Reference No', 'Closing Date', 'Bid Opening Date'])
data_frame.to_csv('TenderData.csv', index=False, encoding='utf-8')
time.sleep(0.5) # Add a delay between requests to avoid overwhelming the website with requests
