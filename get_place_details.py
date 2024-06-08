#This file retrieves detailed information about a specific place, 
#including its reviews, opening hours, photos, etc. This can be achieved using the Google Places Details API.
import requests # type: ignore

# Your API key (replace with your actual API key)
API_KEY = 'INSERT GOOGLE API KEY HERE'

# Function to get place details
def get_place_details(place_id):
    # Endpoint URL for the Places Details API
    url = "https://maps.googleapis.com/maps/api/place/details/json"

    # Parameters for the API request
    params = {
        'place_id': place_id,
        'key': API_KEY
    }

    # Make the request to the Google Places Details API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'result' in data:
            place_details = data['result']
            print("Place Details:")
            print(f"Name: {place_details['name']}")
            print(f"Address: {place_details['formatted_address']}")
            print(f"Phone Number: {place_details.get('formatted_phone_number', 'N/A')}")
            print(f"Website: {place_details.get('website', 'N/A')}")
            print(f"Rating: {place_details.get('rating', 'N/A')}")
            print(f"User Ratings Total: {place_details.get('user_ratings_total', 'N/A')}")
            print(f"Opening Hours: {place_details.get('opening_hours', {}).get('weekday_text', 'N/A')}")
            print("Reviews:")
            for review in place_details.get('reviews', []):
                print(f"Author: {review['author_name']}")
                print(f"Rating: {review['rating']}")
                print(f"Text: {review['text']}")
                print("="*40)
        else:
            print("No place details found.")
    else:
        print(f"Error: {response.status_code}")

# Example place ID (replace with an actual place ID)
example_place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'

# Get details of the example place
get_place_details(example_place_id)
