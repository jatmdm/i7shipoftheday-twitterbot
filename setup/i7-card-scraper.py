# i7-card-scraper.py
import re
import requests
import io
from bs4 import BeautifulSoup

permanent_url = "http://idolish-seven.tumblr.com/permanent"
# limited_url = "http://idolish-seven.tumblr.com/limited"

# Scrape permanents
response = requests.get(permanent_url)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

img_urls = [img['src'] for img in img_tags]

# saving for writing to csv file
image_list = []

# print(img_urls)

for url in img_urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
        image_list.append(url)
       	print(url)


csv_path = "i7-cards.csv"

with open(csv_path, "w") as csvfile:
	csvfile.write("filename, cast (separate by commas),")
	for i in image_list:
		line = i +","
		csvfile.write(line)

print("done...")


# TODO: Make I7 Card class

# class I7Card:

# 	def __init__(self, CastList, url):
