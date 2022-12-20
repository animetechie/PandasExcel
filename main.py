import pandas as pd

# Load the first spreadsheet
df1 = pd.read_excel('spreadsheet1.xlsx')

# Load the second spreadsheet
df2 = pd.read_excel('spreadsheet2.xlsx')

# Combine the two spreadsheets
df = pd.concat([df1, df2])

# Remove duplicate rows
df = df.drop_duplicates()

# Save the combined and deduplicated data to a new Excel file
df.to_excel('combined_spreadsheets.xlsx', index=False)
