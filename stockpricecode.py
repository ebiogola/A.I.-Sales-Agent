import pandas as pd

# Specify the path to your text file
text_file_path = 'C:\\Users\\ebiog\\OneDrive\\Documents\\Master projects\\A.I. Sales Agent\\stockprice_text.txt'

# Read the text file into a pandas DataFrame
df = pd.read_csv(text_file_path, delimiter='\t')  # Adjust the delimiter based on your text file format

# Specify the path to save the Excel file
excel_file_path = 'C:\\Users\\ebiog\\OneDrive\\Documents\\Master projects\\A.I. Sales Agent\\stockprice.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)