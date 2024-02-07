import json

# List of JSON files to check
json_files = ['home.json', 'leisure.json', 'transportation.json', 'insurance.json', 'Pharm.json', 'Business.json',
              'mortgage.json', 'Other.json']

# Load data from output.json
with open('output.json', 'r', encoding='utf-8') as output_file:
    output_data = json.load(output_file)

# Iterate over each JSON file
for file_name in json_files:
    with open(file_name, 'r', encoding='ISO-8859-1') as file:
        file_data = json.load(file)
        # Check if file_data is a list of dictionaries
        if isinstance(file_data, list):
            # Iterate through each expense in the list
            for expense in file_data:
                description = expense.get("Description")
                if description is not None:
                    # Iterate over each entry in output.json
                    for entry in output_data:
                        output_description = entry["Description"].lower() if entry.get("Description") else None
                        if output_description == description.lower():
                            # Add the flag to the entry in output.json
                            flag = entry.get("Flag", [])  # Get existing flag or an empty list if no flag exists
                            flag.append(file_name.split('.')[0])  # Add the file name without the extension to the flag list
                            entry["Flag"] = flag
                            break

# Check if any description has no flag, and if so, add a "None" flag
for entry in output_data:
    if "Flag" not in entry:
        entry["Flag"] = ["None"]

# Write the updated data back to output.json
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)
