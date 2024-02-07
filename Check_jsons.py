import json

# List of all JSON files to check against
json_files = ['home.json', 'leisure.json', 'transportation.json', 'insurance.json', 'Pharm.json', 'Business.json', 'mortgage.json', 'Other.json']

# Load data from all JSON files
data = {}
for file_name in json_files:
    with open(file_name, 'r', encoding='ISO-8859-1') as file:
        data[file_name] = json.load(file)

# Create a set of existing descriptions for faster lookup
existing_descriptions = set()
for file_name, file_data in data.items():
    existing_descriptions.update(expense["Description"] for expense in file_data["expenses"])

# Load data from output.json
with open('output.json', 'r', encoding='utf-8') as output_file:
    output_data = json.load(output_file)

# Iterate through each entry in output.json
for entry in output_data:
    description = entry["Description"]
    # Check if the description exists in any of the JSON files
    if description in existing_descriptions:
        # Iterate through each JSON file
        for file_name, file_data in data.items():
            for expense in file_data["expenses"]:
                if expense["Description"] == description:
                    # Print the existing value
                    print("Existing value for", description, "in", file_name, ":", expense["Amount"])
                    # Check if Flag already exists, if not add it
                    if "Flag" not in entry:
                        entry["Flag"] = []
                    # Add the flag to the entry in output.json
                    entry["Flag"].append(file_name.split('.')[0])
                    break
    else:
        # If no match found, mark Flag as "None"
        entry["Flag"] = "None"

# Write the updated data back to output.json
with open('output2.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)
