import pandas as pd

# Define the source file path
source_file_path = 'sponsorTimes.csv'

# Define the destination file path
destination_file_path = 'output.csv'

# Read the first 4 lines of the csv file
df = pd.read_csv(source_file_path, nrows=20)

# Write the first 4 lines to a new csv file
df.to_csv(destination_file_path, index=False)
