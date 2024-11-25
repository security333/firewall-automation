import pandas as pd

# Load the CSV file
input_file = '/mnt/data/split.csv'

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(input_file)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Check if 'Network' column exists
if 'Network' not in df.columns:
    print("Error: The CSV file does not contain a 'Network' column.")
    exit()

# Get unique values in the 'Network' column
networks = df['Network'].unique()

# Split the data by 'Network' and save to separate CSV files
output_path = '/mnt/data/'
for network in networks:
    # Filter rows for the current network
    filtered_df = df[df['Network'] == network]
    
    # Construct output filename
    output_file = f"{output_path}{network.lower()}.csv"
    
    # Save the filtered data to a CSV file
    try:
        filtered_df.to_csv(output_file, index=False)
        print(f"Created file: {output_file}")
    except Exception as e:
        print(f"Error writing file {output_file}: {e}")
