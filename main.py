import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

#API Information
API_KEY = os.getenv("RC_KEY2")

API_URL = "https://api.restcountries.com/countries/v5"  # Replace with your chosen API endpoint

headers = {'Authorization': API_KEY}

#def display_results(matching_countries):
   
#Fetch data from the API. Returns the raw JSON response, or an empty list on failure
def fetch_countries(params):
    try: 
        response = requests.get(API_URL,headers=headers,params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"Error: Could not reach the server due to the following error {error}. Check your connection and try again.")
        return[]
    
# Extract and transform the fields you need. Returns a list of dictionaries.
def clean_countries(countries_list):

    cleaned = []

    for country in countries_list:
        country_cleaned_data = {
            "name": country["names"]["common"],
            "capital": country["capitals"][0]["name"] if country.get("capitals") else "N/A",
            "continents": country["continents"],
            "region": country["region"],
            "subregion": country["subregion"],
            "population": country["population"],
            "languages": country["languages"],           
            "currencies": country["currencies"],
            "government_type": country["government_type"],            
            "memberships": country["memberships"],
        }

        cleaned.append(country_cleaned_data)

    return cleaned

