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
filtered_lines_for_500_split_and_2k = [line for line in filtered_lines_for_500_split if not pd.isna(line[16])]

# Display or use the filtered lines as needed
print("Number of filtered lines: ", len(filtered_lines_for_500_split))
print("Number of filtered lines: ", len(filtered_lines_for_500_split_and_2k))
#print(filtered_lines)
#Display the complete lines in a table

# table = PrettyTable(df.columns.tolist())  # Convert to list explicitly
# for line in filtered_lines:
#     table.add_row(line)

# print(table)