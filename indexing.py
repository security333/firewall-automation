import os

# Function to increment the index
def increment_index(index):
    prefix, suffix = index.split('-')
    number, sub_number = map(int, suffix.split('.'))
    sub_number += 1
    if sub_number == 100:  # Assuming we reset to 00 when sub_number reaches 100
        number += 1
        sub_number = 0
    return f"{prefix}-{number:02d}.{sub_number:02d}"

# Example usage
file_name = "001-00.txt"  # Example file name
file_name_parts = os.path.splitext(file_name)
new_index = increment_index(file_name_parts[0])
new_file_name = f"{new_index}{file_name_parts[1]}"

print("Original file name:", file_name)
print("New file name:", new_file_name)
