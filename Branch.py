import json
import csv
import random
import uuid
from faker import Faker

fake = Faker()

# Function to generate fake US address
def generate_fake_us_address():
    fake_us_address = fake.address()
    lines = fake_us_address.split('\n')
    
    # Extract numeric part of ZIP code
    zip_code_numeric = ''.join(filter(str.isdigit, lines[-1].split(', ')[-1]))
    
    # Ensure there are enough components to extract state
    if len(lines[-1].split(', ')) >= 2:
        branch_state = lines[-1].split(', ')[-2]
    else:
        branch_state = ""
    
    return {
        "Branch_Full_address": fake_us_address,
        "Branch_address_line_1": lines[0],
        "Branch_address_line_2": lines[1] if len(lines) > 1 else "",
        "Branch_city": lines[-1].split(', ')[0],
        "county": lines[-1].split(', ')[1] if len(lines[-1].split(', ')) > 1 else "",
        "Branch_state": branch_state,
        "Branch_country": "United States",
        "Branch_zip": int(zip_code_numeric)
    }

# Generate Bank Branch data
def generate_branch_data(parent_branch_id=None):
    branch_types = [
        "Retail", "Corporate", "Private", "Online/Internet",
        "Mobile", "Specialized/Theme", "International", "Community",
        "Digital", "Non-Traditional/Branchless", "Wealth Management",
        "Satellite/Office", "Financial Supermarket"
    ]

    branch_id = str(uuid.uuid4())[:6].upper()  # First 6 characters of a UUID4 as an alphanumeric branch_id
    
    return {
        "Branch_id": branch_id,
        "Branch_name": fake.company(),
        "Branch_type": random.choice(branch_types),
        **generate_fake_us_address(),
        "Parent_branch_Id": parent_branch_id
    }

# Generate 100 rows of Bank Branch data
branch_data_list = []

for i in range(15000):
    parent_branch_id = random.choice([None] + [branch["Branch_id"] for branch in branch_data_list])
    branch_data_list.append(generate_branch_data(parent_branch_id))

# Write data to JSON file
json_file_path = '../OutputFiles/Branch.json'
with open(json_file_path, 'w') as jsonfile:
    json.dump(branch_data_list, jsonfile, indent=2)

# Write data to CSV file
csv_file_path = '../OutputFiles/Branch.csv'
csv_headers = list(branch_data_list[0].keys())

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(branch_data_list)
