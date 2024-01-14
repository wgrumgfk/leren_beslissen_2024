import pandas as pd
import os
import matplotlib.pyplot as plt
from statistics import mean
from prettytable import PrettyTable


cwd = os.getcwd()
print(cwd)

csv_path = "okeanos.csv"
df = pd.read_csv(csv_path, delimiter=',', na_values=['', 'NA', 'N/A', 'NaN', 'nan'])
df.head()

# Drop rows with all missing values (NaN) and store the complete lines in a list
complete_lines = df.dropna(how='all', subset=df.columns.tolist()).values.tolist()

# Filter out rows where the value at position 500_split is NaN
filtered_lines_for_500_split = [line for line in complete_lines if not pd.isna(line[8])]


# Filter out rows where the value at position 500_split is NaN and 2k is nan
filtered_lines_for_500_split_and_2k = [line for line in filtered_lines_for_500_split if not pd.isna(line[-2])]

# Display or use the filtered lines as needed
print("Number of filtered lines: ", len(filtered_lines_for_500_split))
print("Number of filtered lines: ", len(filtered_lines_for_500_split_and_2k))
#print(filtered_lines)
#Display the complete lines in a table

# table = PrettyTable(df.columns.tolist())  # Convert to list explicitly
# for line in filtered_lines:
#     table.add_row(line)

# print(table)


split_500_tijden =[line[8] for line in filtered_lines_for_500_split_and_2k] 
_2k_tijden = [line[-2] for line in filtered_lines_for_500_split_and_2k]

print(len(split_500_tijden))
print(len(_2k_tijden))

def entry_to_seconds(entry):
    if pd.isna(entry):
        return None

    # Define your processing logic for each type of entry
    if ':' in entry and '.' in entry:
        # Process entries like '1:47.4'
        parts = entry.split(':')
        minutes = pd.to_numeric(parts[0])
        seconds = pd.to_numeric(parts[1].replace(',', '.'))
        return minutes * 60 + seconds
    elif ':' in entry and ',' in entry:
        # Process entries like '1:47,4'
        parts = entry.split(':')
        minutes = pd.to_numeric(parts[0])
        seconds = pd.to_numeric(parts[1].replace(',', '.'))
        return minutes * 60 + seconds
    elif '.' in entry:
        # Process entries like '1.45.5'
        parts = entry.split('.')
        minutes = pd.to_numeric(parts[0])
        seconds = pd.to_numeric(parts[1])
        return minutes * 60 + seconds
    else:
        # Handle other cases
        raise ValueError("Invalid time string format")

def seconds_to_wattage(df, column_name):
    # Apply the entry_to_seconds function to the specified column
    return 2.8 / df[column_name].apply(entry_to_seconds) ** 3

df.loc[:, 'wattage'] = seconds_to_wattage(df, '500_split')


