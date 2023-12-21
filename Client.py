import json
import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate random date within a given range
def random_date(start_date, end_date):
    return fake.date_time_between_dates(datetime_start=start_date, datetime_end=end_date)

start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 31)

def generate_fake_phone_number():
    return fake.phone_number()

def generate_fake_email():
    return fake.email()

# Generate Client data
def generate_client_data(client_id):
    create_date = random_date(start_date, end_date)
    update_date = create_date + timedelta(days=random.randint(1, 30))
    
    investment_objectives = [
        "Capital Preservation",
        "Income Generation",
        "Capital Appreciation",
        "Wealth Accumulation",
        "Risk Tolerance",
        "Retirement Planning",
        "Tax Efficiency",
        "Liquidity Needs",
        "Socially Responsible Investing (SRI)",
        "Education Funding"
    ]
    
    return {
        "ClientID": client_id,
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "DateOfBirth": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d"),
        "Gender": random.choice(["Male", "Female"]),
        "Citizenship": fake.country(),
        "MaritalStatus": random.choice(["Single", "Married", "Divorced", "N/A"]),
        "isSelfEmployed": fake.boolean(),
        "EmploymentStatus": fake.random_element(["Employed", "Unemployed", "Business"]),
        "Employer": fake.company(),
        "Occupation": fake.job(),
        "Income": round(random.uniform(30000, 120000), 2),
        "NetWorth": round(random.uniform(50000, 5000000), 2),
        "InvestmentExperience": random.randint(1, 10),
        "RiskTolerance": random.choice(["Low", "Medium", "High"]),
        "InvestmentObjectives": random.choice(investment_objectives),
        "RelationshipManagerID": fake.uuid4(),
        "CreationDate": create_date.strftime("%Y-%m-%d %H:%M:%S"),
        "LastUpdateDate": update_date.strftime("%Y-%m-%d %H:%M:%S"),
        "LastKYCDate": update_date.strftime("%Y-%m-%d %H:%M:%S"),
        "isDeceased": fake.boolean(),
        "Country_of_residence": fake.country()
    }

def generate_fake_us_address():
    fake = Faker('en_US')  # Set the locale to U.S. English
    return fake.address()

def split_address_components(address):
    lines = address.split('\n')
    address_line1 = lines[0]
    address_line2 = lines[1] if len(lines) > 1 else ""  # Address Line 2 is optional
    
    # Split city, state, and ZIP code
    city_state_zip = lines[-1].split(', ')
    
    if len(city_state_zip) == 2:
        city, state_zip = city_state_zip
        state, zip_code = state_zip.split(' ')
    elif len(city_state_zip) == 1:
        city = city_state_zip[0]
        state = ""
        zip_code = ""
    else:
        raise ValueError("Invalid address format")
    
    return address_line1, address_line2, city, state, zip_code

# Generate Client_Phone, Client_Email, and Client_Address data
def generate_contact_data(client_id):
    phone_types = ["Primary", "Communication", "Secondary"]
    address_types = ["Primary", "Communication", "Secondary"]
    create_date = random_date(start_date, end_date)
    update_date = create_date + timedelta(days=random.randint(1, 30))
    fake_us_address = generate_fake_us_address()
    address_line1, address_line2, city, state, zip_code = split_address_components(fake_us_address)
    
    return {
        "Phone_id": fake.uuid4(),
        "Phone_type": random.choice(phone_types),
        "Client_id": client_id,
        "Phone_Number": generate_fake_phone_number(),
        "Row_create_date": create_date.strftime("%Y-%m-%d %H:%M:%S"),
        "Row_update_date": update_date.strftime("%Y-%m-%d %H:%M:%S"),
        "is_active": random.randint(0, 1),
    }, {
        "Email_id": fake.uuid4(),
        "Email_type": random.choice(address_types),
        "Client_id": client_id,
        "Email_Address": generate_fake_email(),
        "Row_create_date": create_date.strftime("%Y-%m-%d %H:%M:%S"),
        "Row_update_date": update_date.strftime("%Y-%m-%d %H:%M:%S"),
        "is_active": random.randint(0, 1),
    }, {
        "Address_id": fake.uuid4(),
        "Address_type": random.choice(address_types),
        "Client_id": client_id,
        "Full_Address": fake_us_address,
        "Address_Line_1": address_line1,
        "Address_Line_2": address_line2,
        "City": city,
        "State": state,
        "Zip": zip_code,
        "Row_create_date": create_date.strftime("%Y-%m-%d %H:%M:%S"),
        "Row_update_date": update_date.strftime("%Y-%m-%d %H:%M:%S"),
        "is_active": random.randint(0, 1),
    }

# Generate 1000 rows of data
client_data_list = []
phone_data_list = []
email_data_list = []
address_data_list = []

for i in range(1000):
    client_id = fake.uuid4()
    client_data_list.append(generate_client_data(client_id))
    phone_data, email_data, address_data = generate_contact_data(client_id)
    phone_data_list.append(phone_data)
    email_data_list.append(email_data)
    address_data_list.append(address_data)


# Write data to CSV files
"""def write_to_csv(data_list, file_name, headers):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_list)

# Write data to CSV files
write_to_csv(client_data_list, './OutputFiles/Client.csv', client_data_list[0].keys())
write_to_csv(phone_data_list, './OutputFiles/Client_Phone.csv', phone_data_list[0].keys())
write_to_csv(email_data_list, './OutputFiles/Client_Email.csv', email_data_list[0].keys())
write_to_csv(address_data_list, './OutputFiles/Client_Address.csv', address_data_list[0].keys())
"""

# Write data to JSON files
def write_to_json(data_list, file_name):
    with open(file_name, 'w') as jsonfile:
        json.dump(data_list, jsonfile, indent=2)

# Write data to JSON files
write_to_json(client_data_list, './OutputFiles/Client.json')
write_to_json(phone_data_list, './OutputFiles/Client_Phone.json')
write_to_json(email_data_list, './OutputFiles/Client_Email.json')
write_to_json(address_data_list, './OutputFiles/Client_Address.json')