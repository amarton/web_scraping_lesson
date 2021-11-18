# -*- coding: utf-8 -*-
"""How to webscrape

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18fFCBOFTJtNZkeAatXNce-DS2qN2kobJ

# Load Libraries
"""

import requests # allow you to send HTTP requests
from bs4 import BeautifulSoup # allows you to parse
import time  # allows you to do things with dates
import csv #allows you to save csv

"""# Set Variables"""

url = "https://www.theguardian.com/us"

"""# Download links to stories on front page

"""

# Download HTML
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Parse HTML and print results
main = soup.find("section", {"id": "headlines"}) # isolate the section of html with the headlines
all_headlines = main.find_all("a") # put all of the a tags into a list

headline_results = [] # create an empyt list to save results in 
url_results = [] # create an empty list to save results in 

# Seperate the url and text from the a tags
for headline in all_headlines: # a for loop that get the url and text for each headline and saves it into a list
  headline_text = headline.text
  url = headline["href"]
  headline_results.append(headline_text)
  url_results.append(url)

"""# Visualize Results"""

#print("Here is the list of headlines")
#print(headline_results)

#print("--------------------")


#print("Here is the list of urls")
#print(url_results)

"""# Save Results"""

# Save html
with open(f'./html_download/guardian_headlines_{time.strftime("%Y%m%d-%H%M%S")}.html', "w") as f:
    f.write(page.text)


# Save csv

file = open(f'./csv_results/guardian_headlines_{time.strftime("%Y%m%d-%H%M%S")}.csv', "w")
headers = ["headline", "url"]
writer = csv.writer(file)
writer.writerow(headers)
for w in range(len(headline_results)):
  writer.writerow([headline_results[w], url_results[w]])
file.close()
