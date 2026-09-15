import requests
import json
import os
import matplotlib.pyplot as plt

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

#matplotlib function
def create_population_chart(countries):

    sorted_countries = sorted(countries, key=lambda country: country["population"], reverse=True)

    top_10_countries = sorted_countries[:10]

    country_names = []
    populations = []

    for country in top_10_countries:
        country_names.append(country["name"])
        populations.append(country["population"] / 1000000)

    plt.barh(country_names, populations)
    plt.gca().invert_yaxis()

    plt.xlabel("Population (Millions)")
    plt.ylabel("Country")
    plt.title("Top 10 Most Populous Countries")
    plt.tight_layout()
    plt.savefig("top_10_population.png")
    plt.show()

#Print Country Explorer Menu
def show_menu():
    print("")
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Search by currency")
    print("4. View population chart")
    print("5. Quit")
    print("")

    option = input("Choose an option (1-5):")
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

    if not countries:
        return

    cleaned_countries = clean_countries(countries["data"]["objects"])


    while True: 
        result = show_menu()
        if result == "1":
            search_term = input("Please enter the country you want information on: ").strip()
            print("")

            #Search for matching countries
            matching_countries = search_countries(cleaned_countries, search_term)

            if not matching_countries:
                print("No matching countries found.")

            else:
                #Sort countries by population
                sorted_search_countries = sorted(
                    matching_countries, key=lambda country: country["population"], reverse=True
                )

                for country in sorted_search_countries:
                    print(f"{country['name']} - Capital: {country['capital']} | Region: {country['region']} | Population: {country['population']} ")              

        elif result == "2":
            region_name = input("Please enter the region name: ").strip()

            region_countries = search_region(cleaned_countries, region_name)

            if not region_countries:
                print("No countries found in that region.")

            else:
                #Sort countries by population
                sorted_cleaned_countries = sorted(
                    region_countries, key=lambda country: country["population"],
                    reverse=True
                )

                for country in sorted_cleaned_countries:
                    print(f"Country: {country['name']} | Capital: {country['capital']} | Region: {country['region']} | Population: {country['population']} ") 

        elif result == "3":
            print("")
            print("Top 10 Currencies in the World:")
            print("USD - United States Dollar")
            print("EUR - Euro")
            print("JPY - Japanese Yen")
            print("GBP - British Pound Sterling")
            print("CNY - Chinese Yuan")
            print("CHF - Swiss Franc")
            print("CAD - Canadian Dollar")
            print("AUD - Australian Dollar")
            print("INR - Indian Rupee")
            print("SGD - Singapore Dollar")
            print("")

            currency_name = input("Enter a currency name or code from the list above: ").strip()
            print("")

            currencies_countries = search_currencies(cleaned_countries, currency_name)

            if not currencies_countries:
                print("No countries found using that currency")

            else:

                #Sort countries by population
                sorted_cleaned_countries = sorted(
                    currencies_countries, key=lambda country: country["name"]
                )

                for country in sorted_cleaned_countries:
                    currency_list =[]
                    other_currencies = []

                    for currency in country["currencies"]:
                        currency_info = f"{currency['name']} ({currency['code']}) {currency['symbol']}"

                        if(currency_name.lower() == currency['name'].lower() or currency_name.lower() == currency['code'].lower()):
                            currency_list.append(currency_info)
                        else:
                            other_currencies.append(currency_info)

                    currency_list.extend(other_currencies)
                    currencies_display = ", ".join(currency_list)
                    print(f"{country['name']} | Currencies: {currencies_display}")            

        elif result == "4":
            create_population_chart(cleaned_countries)

        elif result == "5":
            quit_loop()
            break

        else:
            print("Please enter a number between 1 and 4.")

main()