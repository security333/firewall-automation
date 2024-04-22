import csv

def load_ip_addresses(filename):
    ip_addresses = set()
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                ip_addresses.add(cell.strip())  # strip whitespace from each cell
    return ip_addresses

def highlight_matches(ip_addresses, input_filename, output_filename):
    with open(input_filename, 'r', newline='') as input_csvfile, \
         open(output_filename, 'w', newline='') as output_csvfile:

        reader = csv.reader(input_csvfile)
        writer = csv.writer(output_csvfile)

        for row in reader:
            new_row = []
            for cell in row:
                if cell.strip() in ip_addresses:
                    new_row.append(f'*{cell}*')  # Add asterisks to highlight
                else:
                    new_row.append(cell)
            writer.writerow(new_row)

if __name__ == "__main__":
    ip_addresses_filename = "ip_addresses.csv"  # File containing IP addresses
    input_filename = "input.csv"  # File to read and highlight matches
    output_filename = "output.csv"  # Output file with matches highlighted

    ip_addresses = load_ip_addresses(ip_addresses_filename)
    highlight_matches(ip_addresses, input_filename, output_filename)
