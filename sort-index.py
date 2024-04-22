import csv

def sort_csv(input_filename, output_filename):
    # Read CSV file and load data into a list of lists
    with open(input_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Get the header row with the numbered index
    header_row = data[0]

    # Sort data based on the indexed column in the first row
    sorted_data = sorted(data[1:], key=lambda x: (int(x[0].split('-')[0]), int(x[0].split('-')[1])))

    # Add the header row back to the sorted data
    sorted_data.insert(0, header_row)

    # Write sorted data to a new CSV file
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_data)

if __name__ == "__main__":
    input_filename = "input.csv"  # Input CSV file to be sorted
    output_filename = "output_sorted.csv"  # Output sorted CSV file

    sort_csv(input_filename, output_filename)
