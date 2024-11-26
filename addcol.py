import pandas as pd

# Load the input CSV file
input_file = '/mnt/data/split - Sheet1.csv'
output_file = '/mnt/data/modified_split.csv'

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Check if required columns exist
    if 'Source' not in df.columns or 'Destination' not in df.columns:
        print("Error: The CSV file must contain 'Source' and 'Destination' columns.")
        exit()

    # Add "Source Group Name" column to the right of "Source"
    source_index = df.columns.get_loc('Source') + 1
    df.insert(source_index, 'Source Group Name', '')

    # Add "Destination Group Name" column to the right of "Destination"
    destination_index = df.columns.get_loc('Destination') + 1
    df.insert(destination_index, 'Destination Group Name', '')

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Modified CSV file saved as: {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")
