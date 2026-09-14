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

#Search for countries information
def search_countries(countries, search_term):            
    search_countries = []

    for country in countries:
        if search_term.lower() in country["name"].lower():
            search_countries.append(country)
    return search_countries

#Search for countries by region
def search_region(countries, region):
    region_countries = []

    #Find countries that match the search region
    for country in countries:
        if country["region"].lower() == region.lower():
            region_countries.append(country)

    return region_countries

#Search for currencies per country
def search_currencies(countries, currency):
    currencies_countries =[]

    #Find the currencies used by countries
    for country in countries:
        for country_currency in country["currencies"]:
            if (currency.lower() == country_currency["name"].lower() or currency.lower() == country_currency["code"].lower()):

                currencies_countries.append(country)
                break

    return currencies_countries

#Print Country Explorer Menu
def show_menu():
    print("")
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Search by currency")
    print("4. Quit")
    print("")

    option = input("Choose an option (1-4):")
    return option

#Quit Country Explorer Loop
def quit_loop():
    print("Quit Country Explorer")
    
def main():

    params = {
            "response_fields": "names.common, capitals, government_type, continents, region, subregion, memberships, population, currencies, languages",
            "limit":100,
        }

    countries = fetch_countries(params)
    print(countries)

main()