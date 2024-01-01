import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# List of URLs of the webpages you want to extract tables from
urls = ["https://afx.kwayisi.org/ngx/", "https://afx.kwayisi.org/ngx/?page=2"]

# Create an empty list to store DataFrames
tables = []

# Iterate over each URL
for url in urls:
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all tables on the webpage using BeautifulSoup
    all_tables = soup.find_all('table')
    
    # Loop through each table and convert it to a DataFrame
    for table in all_tables:
        df = pd.read_html(str(table))[0]
        tables.append(df)

# If you want to save each DataFrame to a separate Excel file
for i, table_df in enumerate(tables, start=1):
    table_df.to_excel(f"table_{i}.xlsx", index=False)

print("Tables extracted and saved to Excel files.")
