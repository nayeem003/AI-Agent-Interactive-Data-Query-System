import pandas as pd
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key (from .env)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

# Google Sheets connection (using the public Google Sheets URL)
def connect_google_sheets(sheet_url):
    """
    Fetch data from a public Google Sheets document using its URL.
    Assumes the sheet is public or accessible via the link.
    """
    # Extract the sheet ID from the URL
    sheet_id = sheet_url.split("/d/")[1].split("/")[0]
    sheet_range = "Sheet1"  # Assuming you want to get data from the first sheet
    
    # Build the Google Sheets API URL
    google_sheets_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{sheet_range}?key={os.getenv('GOOGLE_API_KEY')}"
    
    # Make a GET request to fetch the sheet data
    response = requests.get(google_sheets_url)
    
    if response.status_code == 200:
        sheet_data = response.json()
        
        # Convert the sheet data to a pandas DataFrame
        values = sheet_data.get('values', [])
        if values:
            # Assuming the first row contains column names
            df = pd.DataFrame(values[1:], columns=values[0])
            return df
        else:
            return pd.DataFrame()  # Return empty dataframe if no data exists
    else:
        return f"Error fetching Google Sheets data: {response.status_code}"

# SerpAPI Connection for Web Search
def get_serpapi_results(query):
    """
    Fetch search results using the SerpAPI.
    """
    url = f"https://serpapi.com/search?q={query}&api_key={SERP_API_KEY}"
    response = requests.get(url)
    return response.json()  # Return the response in JSON format
