#This file is useful for searching for restaurants in NYC.

import pandas as pd
import json
import requests # type: ignore

import requests # type: ignore

# Your API key (replace with your actual API key)
API_KEY = 'AIzaSyDBddhnVsgh3JZLog2Z_HvAs1a-VZ3MwvM'

# Endpoint URL for the Places API Text Search
url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Parameters for the API request
#Define the parameters for your API request. In this example, 
# the query is to search for restaurants in New York.
params = {
    'query': 'restaurants in New York',
    'key': API_KEY
}

# Make the get request to the Google Maps Places API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    if 'results' in data:
        places = data['results']
        for place in places:
            print(f"Name: {place['name']}")
            print(f"Address: {place['formatted_address']}")
            print(f"Place ID: {place['place_id']}")
            print("="*40)
    else:
        print("No results found.")
else:
    print(f"Error: {response.status_code}")