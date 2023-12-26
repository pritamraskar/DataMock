import json
import csv
import random
from faker import Faker

fake = Faker()

# Load existing Branch data from Branch.json
def load_branch_data(file_name):
    with open(file_name, 'r') as jsonfile:
        branch_data = json.load(jsonfile)
    return [branch["Branch_id"] for branch in branch_data]

# Function to generate a valid RM ID
def generate_rm_id():
    return "RM" + fake.uuid4().replace("-", "")[:6].upper()

# Function to split full name into first name, last name, and middle name
def split_full_name(full_name):
    names = full_name.split()
    rm_firstname = names[0] if names else ""
    rm_lastname = names[-1] if names else ""
    rm_middlename = ' '.join(names[1:-1]) if len(names) > 2 else ""
    return rm_firstname, rm_lastname, rm_middlename

# Function to generate Relationship Manager data
def generate_rm_data(branch_ids, existing_rm_ids):
    full_name = fake.name()
    rm_firstname, rm_lastname, rm_middlename = split_full_name(full_name)
    rm_branch = random.choice(branch_ids)
    is_branch_manager = fake.boolean()
    is_independent = fake.boolean()
    license = ""
    registration_state = ""
    
    # Ensure primary_id and secondary_id are different existing_rm_ids
    primary_id, secondary_id = random.sample(existing_rm_ids, k=2)
    
    other_id = None
    is_employee = fake.boolean()
    employee_id = generate_rm_id() if is_employee else None

    return {
        "rm_id": generate_rm_id(),
        "rm_name": full_name,
        "rm_firstname": rm_firstname,
        "rm_lastname": rm_lastname,
        "rm_middlename": rm_middlename,
        "rm_branch": rm_branch,
        "isBranchManager": is_branch_manager,
        "isIndependent": is_independent,
        "license": license,
        "registration_state": registration_state,
        "primary_id": primary_id,
        "secondary_id": secondary_id,
        "other_id": other_id,
        "isEmployee": is_employee,
        "employee_id": employee_id
    }

# Generate Relationship Manager data
def generate_relationship_manager_data(num_records, branch_ids, existing_rm_ids):
    rm_data_list = []

    for _ in range(num_records):
        rm_data_list.append(generate_rm_data(branch_ids, existing_rm_ids))

    return rm_data_list

# Example: Load existing Branch IDs from Branch.json
branch_ids_example = load_branch_data('./OutputFiles/Branch.json')  # Update the path

# Example: Assume there are existing Relationship Managers with IDs like 'RM001', 'RM002', ..., 'RM010'
existing_rm_ids_example = ['RM{:03}'.format(i) for i in range(1, 11)]

# Generate 100 rows of Relationship Manager data
rm_data_list_example = generate_relationship_manager_data(10000, branch_ids_example, existing_rm_ids_example)

# Write data to JSON file
def write_to_json(data_list, file_name):
    with open(file_name, 'w') as jsonfile:
        json.dump(data_list, jsonfile, indent=2)

# Write data to JSON file inside the "./OutputFiles/" directory
write_to_json(rm_data_list_example, './OutputFiles/Relationship_Manager.json')  # Update the path


# Write data to CSV file
csv_file_path = './OutputFiles/Relationship_Manager.csv'
csv_headers = list(rm_data_list_example[0].keys())

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(rm_data_list_example)
