# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 16:05:36 2025

@author: PC1
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup


def web_scraper():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup.title)
    
    
    price = soup.find_all(string=lambda text: text and '£' in text)
    print(price[:5])
    filtered_links =[]
    target_categories = ['travel', 'health', 'romance', 'religion']
    catagory_links = soup.find_all('a',href =lambda href:href and '/books/' in href)
    price = soup.find_all('div.prouduct_price')
    
    file = open('books', 'w')
    
    for link in catagory_links:
       
     
        link_name = link.text.strip().lower()
        
        if any(category in link_name for category in target_categories):
            filtered_links.append(link)
            print(f"found: {link_name}")
    print(f"Total filtered links: {len(filtered_links)}")
    
    
    for link in filtered_links:
        catagory_url = "https://books.toscrape.com/" + link['href']
        
        catagory_res = requests.get(catagory_url)
        catagory_soup = BeautifulSoup(catagory_res.text, 'html.parser')
     
        prices = catagory_soup.find_all('p',class_='price_color')
        
        #priting to file
        file.write(f"Catagory :{link.text.strip()}")
        file.write(f"found:{len(prices)} books")
        
        #priting to console
        print(f"Catagory :{link.text.strip()}")
        print(f"found:{len(prices)} books")
        for price in prices[:3]:
            
            file.write(f"prices:{price.text}")
            print(f"prices:{price.text}")
        file.write("\n")
    
    
    file.close()
    
web_scraper()