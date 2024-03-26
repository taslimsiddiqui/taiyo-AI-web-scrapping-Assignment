#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import pandas as pd
from PIL import Image
import io
from bs4 import BeautifulSoup
import time


# In[ ]:


# Create an empty DataFrame to store the collected data
data_frame = pd.DataFrame()


# In[ ]:


driver=webdriver.Chrome('chromedriver.exe')

# Navigate to the initial webpage
webpage_url = "https://etenders.gov.in/eprocure/app?page=FrontEndLatestActiveTenders&service=page"
driver.get(webpage_url)




# Maximum number of CAPTCHA retries
max_retries = 3

while True:
    retries = 0  # Initialize the retries counter
    captcha_successful = False  # Flag to track successful CAPTCHA entry
    
    while retries < max_retries:
        # Capture and process the CAPTCHA
        element_to_capture = driver.find_element_by_id("captchaImage")
        element_location = element_to_capture.location
        element_size = element_to_capture.size

        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot))
        left = element_location['x']
        top = element_location['y']
        width = element_size['width']
        height = element_size['height']
        element_screenshot = image.crop((left, top, left + width, top + height))

        element_screenshot_path = "element_screenshot.png"
        element_screenshot.save(element_screenshot_path)

        url = "https://api.ocr.space/parse/image"
        data = {
            "apikey": "K81476627888957",  # Replace with your OCR.space API key
            "language": "eng",
            "filetype": "PNG",
            "IsOverlayRequired": False,
            "IsTable": False,
            "IsCreateSearchablePdf": False,
            "IsSearchablePdfHideTextLayer": True
        }

        with open(element_screenshot_path, 'rb') as image_file:
            files = {"file": (element_screenshot_path, image_file)}
            response = requests.post(url, data=data, files=files)

        result = response.json()
        parsed_text = result['ParsedResults'][0]['ParsedText']
        parsed_text = parsed_text.replace(" ", "")
        captcha_input = driver.find_element_by_id("captchaText")
        captcha_input.clear()
        captcha_input.send_keys(parsed_text)

        # Check if CAPTCHA entry was successful
        if "Please enter the text as shown" not in driver.page_source:
            captcha_successful = True
            break  # Exit the CAPTCHA retry loop
        
        # Increment the retries counter and add a delay before the next retry
        retries += 1
        time.sleep(5)  # Add a 2-second delay between retries
    
    if not captcha_successful:
        print("CAPTCHA entry failed after {} retries. Exiting.".format(max_retries))
        break  # Exit the main loop if CAPTCHA entry fails repeatedly

    try:
        # Extract and process data from the page
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        table = soup.find('table', {'id': 'table'})
        table_data = []

        rows = table.find_all('tr', {'class': ['even', 'odd']})

        for row in rows:
            cells = row.find_all('td')
            row_data = [cell.get_text(strip=True) for cell in cells]
            table_data.append(row_data)

        # Append the data to the data frame
        if len(table_data) > 0:
            df = pd.DataFrame(table_data)
            data_frame = data_frame.append(df, ignore_index=True)

        # Find the "Forward" link element by its id
        forward_link = driver.find_element_by_id("linkFwd")

        try:
            # Click on the "Forward" link to navigate to the next page
            forward_link.click()
        except:
            # If there's no more next page, break out of the loop
            break

        # Add a time delay (e.g., 2 seconds) after each process
        time.sleep(3)
    except AttributeError:
        # Handle the case where the table is not found on the page
        
        print("Table not found on this page. Refill Captcha.")
        
        try:
            
            clear_link=driver.find_element_by_id("clear")
            clear_link.click()

        except:
            # If there's no more next page, break out of the loop
            print("No more pages to navigate to. Exiting.")
            break


# In[ ]:


data_frame


# In[ ]:


data_frame.to_csv('tender.csv')

