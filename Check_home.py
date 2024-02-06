import json

# Load data from output.json
with open('output.json', 'r', encoding='utf-8') as output_file:
    output_data = json.load(output_file)

# Load data from home.json
with open('home.json', 'r', encoding='ISO-8859-1') as home_file:
    home_data = json.load(home_file)

# Create a set of existing descriptions in home.json for faster lookup
home_descriptions = {expense["Description"] for expense in home_data["expenses"]}

# Iterate through each entry in output.json
for entry in output_data:
    description = entry["Description"]
    # Check if the description exists in home.json
    if description in home_descriptions:
        # Find the corresponding entry in home.json
        for expense in home_data["expenses"]:
            if expense["Description"] == description:
                # Print the existing value
                print("Existing value for", description, ":", expense["Amount"])
                # Add the flag "home" to the entry in output.json
                entry["Flag"] = "home"
                break

# Write the updated data back to output.json
with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)
