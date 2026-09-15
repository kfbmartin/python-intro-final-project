# Project Title: Country Explorer

Country Explorer allows for users to interact with the REST Countries API.  Users search and filter countries by the country name, region and currency.  The program can be run via the command-line interface (CLI) in the terminal. 

Due to the limitations of the free API plan, Country Explorer retrieves a maximum of 100 country per request, so the program currently searches and filters only those 100 records rather than the complete list of countries.

## API

This project uses the REST Countries API: https://api.restcountries.com/countries/v5

## Installation

1. Clone this repository:

   git clone https://github.com/kfbmartin/python-intro-final-project.git
   cd python-intro-final-project


2. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows
  
3. Install dependencies:

   pip install -r requirements.txt

## Usage
Run the program with:
python main.py


When the programs runs, it fetches the country information from the REST Countries API and displays the Country Explorer menu. The user can search for a country by name, filter coountries by region, search by currency or quit the program.

After the user makes a selection and enters the requested search information, the program displays the matching countries and relevant information in the terminal. The Country Explorer menu is then displayed again so the user can perform another search or quit the program.

If a search does not return any matching countries, the program displays a message explaining that no matches were found. If the user enters an invalid menu option, the program asks the user to enter a number between 1 and 4 and displays the menu again.

## CLI Interactions

- **Search by name** — Enter all or part of a country name. The program displays matching countries along with the capital, region, and population. The countries are return in the order of population
- **Filter by region** — Enter a region name. The program displays countries in that region and sorts the results by population from largest to smallest.
- **Search by currency** — Enter a currency name or currency code, such as USD or EUR. The program displays countries that use the selected currency and shows the currencies used by each matching country. The countries are returned in alphabetical order.
- **Quit** — enter a currency name or code to see countries that use that currency

