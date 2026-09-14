# Project Title: Country Explorer

The country explorer allows for users to interact with the REST Countries API.  The user will be about to search and filter countries by the country name, region and currency.  The program can be run via the commandline in the terminal. 

Due to the limitations of the free API plan, Country Explorer retrieves a maximum of 100 country per request, so the program currently searches and filters only those 100 records rather than the complete list of countries.

## API

This project uses the REST Countries (https://api.restcountries.com/countries/v5) API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kfbmartin/python-intro-final-project.git
   cd python-intro-final-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

Describe what happens when the program runs — what prompt(s) appear and what the user can do.

When the programs runs, it fetches the country information from the REST Countries API and displays the Country Explorer menu. The user can search for a country by name, filter coountries by region, search by currency or quit the program.

After the user enters a selection, the program displays the matching countries and their relevant information in the terminal and then promps the user to make another selection until they quit they quit the program.

If the user enters incorrect information after making their selection they will be prompted again and again until they enter correct information.

## CLI Interactions

Describe each interaction your CLI supports. For example:

- **Filter by region** — enter a region name to see all matching records
- **Search by name** — enter a name to see details for one specific record
- **Search by currency** — enter a currency name or code to see countries that use that currency

