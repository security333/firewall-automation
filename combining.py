

# Constructing the path pattern for files to be read
file_pattern = os.path.join(working_ticket, "*-extratedIPs.txt")

# List to store content from all files
all_content = []

# Reading content from all files matching the pattern
for file_name in glob.glob(file_pattern):
    with open(file_name, "r") as file:
        all_content.append(file.read())

# Writing combined content to a new file
combined_file_path = os.path.join(working_ticket, "extractedIPs-combined.txt")
with open(combined_file_path, "w") as combined_file:
    combined_file.write("\n".join(all_content))



# Read content from the file
with open(os.path.join(working_ticket, "extractedIPs-combined.txt"), "r") as file:
    content = file.readlines()

# Filter out empty lines
filtered_content = [line.strip() for line in content if line.strip()]

# Write filtered content back to the file
with open(os.path.join(working_ticket, "extractedIPs-combined.txt"), "w") as file:
    file.write("\n".join(filtered_content))
