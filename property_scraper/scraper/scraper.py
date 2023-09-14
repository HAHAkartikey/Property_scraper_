# scraper/scraper.py

import requests
from bs4 import BeautifulSoup
from .models import Property
from django.conf import settings

def scrape_property_data(url):
    # Make a GET request to the property page
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract property details from the page
        name = soup.find('h1').text.strip()
        cost = float(soup.find('span', {'class': 'property-price'}).text.strip().replace('₹', '').replace('L', ''))
        property_type = soup.find('span', {'class': 'property-type'}).text.strip()
        area = float(soup.find('span', {'class': 'property-size'}).text.strip().split(' ')[0])

        # Save the data to the database
        property_obj = Property(name=name, cost=cost, property_type=property_type, area=area, link=url)
        property_obj.save()
    else:
        print(f"Failed to fetch data from {url}")

scrape_property_data('https://www.99acres.com/sample-property-url')

    # Store the data in MongoDB
property_dict = {
    "name": name,
    "cost": cost,
    "property_type": property_type,
    "area": area,
    "link": url
}
    
settings.mongo_db.properties.insert_one(property_dict)