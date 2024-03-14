import json
import random
from faker import Faker
from datetime import datetime, timedelta
import uuid

fake = Faker()

def load_branch_data(file_name):
    with open(file_name, 'r') as jsonfile:
        branch_data = json.load(jsonfile)
    return [branch["Branch_id"] for branch in branch_data]

def generate_scenario_data():
    scenario_id = fake.uuid4().hex[:16].upper()
    scenario_name = fake.word()
    threshold_value = round(random.uniform(0, 100), 2)
    actual_value = round(random.uniform(0, 100), 2)
    score = round(random.uniform(0, 100), 2)

    return {
        "Scenario_Id": scenario_id,
        "Scenario_Name": scenario_name,
        "Threshold_Value": threshold_value,
        "Actual_Value": actual_value,
        "Score": score
    }

def generate_focus_details():
    focus_types = ["Technical", "Process"]
    focus_names = ["Code Quality", "Delivery Efficiency"]
    focus_descriptions = ["Measures the quality of the codebase", "Measures the efficiency of the delivery process"]
    
    focus_details = []
    for focus_type, focus_name, focus_description in zip(focus_types, focus_names, focus_descriptions):
        scenarios = []
        if focus_type == "Technical":
            scenarios = [
                {
                    "Scenario_Id": "SC001",
                    "Scenario_Name": "Unit Test Coverage",
                    "Threshold_Value": 80,
                    "Actual_Value": 90,
                    "Score": 100
                },
                {
                    "Scenario_Id": "SC002",
                    "Scenario_Name": "Code Duplication",
                    "Threshold_Value": 15,
                    "Actual_Value": 10,
                    "Score": 90
                },
                {
                    "Scenario_Id": "SC003",
                    "Scenario_Name": "Code Complexity",
                    "Threshold_Value": 20,
                    "Actual_Value": 18,
                    "Score": 65
                }
            ]
        elif focus_type == "Process":
            scenarios = [
                {
                    "Scenario_Id": "SC004",
                    "Scenario_Name": "Lead Time",
                    "Threshold_Value": 10,
                    "Actual_Value": 8,
                    "Score": 80
                },
                {
                    "Scenario_Id": "SC005",
                    "Scenario_Name": "Deployment Frequency",
                    "Threshold_Value": 4,
                    "Actual_Value": 3,
                    "Score": 70
                },
                {
                    "Scenario_Id": "SC006",
                    "Scenario_Name": "Change Failure Rate",
                    "Threshold_Value": 5,
                    "Actual_Value": 3,
                    "Score": 75
                }
            ]
        
        total_score = sum(scenario["Score"] for scenario in scenarios)
        focus_detail = {
            "Focus_Type": focus_type,
            "Focus_Name": focus_name,
            "Focus_Description": focus_description,
            "Total_Score": total_score,
            "Scenarios": scenarios
        }
        focus_details.append(focus_detail)
    
    return json.dumps({"Focus": focus_details})

# Function to generate running numbers from 00001 to 99999
def generate_running_numbers():
    for i in range(1, 100000):
        yield f"{i:05d}"

# Create a generator for running numbers
running_numbers = generate_running_numbers()

def generate_alert_data(num_records, branch_ids):
    alert_types = ["Type1", "Type2", "Type3"]
    status_ids = ["Status1", "Status2", "Status3"]
    business_units = branch_ids
    business_unit_families = ["Family1", "Family2", "Family3"]
    business_unit_families_previous = ["PreviousFamily1", "PreviousFamily2", "PreviousFamily3"]
    details = ["Detail1", "Detail2", "Detail3"]
    states = ["State1", "State2", "State3"]
    business_dates = [fake.date_between(start_date="-3y", end_date="today") for _ in range(num_records)]
    create_dates = [fake.date_time_between_dates(datetime_start=datetime(2021, 1, 1), datetime_end=datetime(2023, 12, 31)).date()
                    for _ in range(num_records)]
    last_update_dates = [fake.date_time_between_dates(datetime_start=datetime(2021, 1, 1), datetime_end=datetime(2023, 12, 31)).date()
                         for _ in range(num_records)]

    alert_data_list = []

    for _ in range(num_records):
        alt_type = random.choice(alert_types)
        alert_data = {
            "alert_id": f"{alt_type}_{next(running_numbers)}",
            "alert_type_id": alt_type,
            "status_id": random.choice(status_ids),
            "deleted": fake.boolean(),
            "business_unit": random.choice(business_units),
            "business_unit_family": random.choice(business_unit_families),
            "business_unit_family_previous": random.choice(business_unit_families_previous),
            "details": random.choice(details),
            "score": round(random.uniform(0, 100), 2),
            "state": random.choice(states),
            "business_date": random.choice(business_dates).strftime("%Y-%m-%d"),
            "create_date": random.choice(create_dates).strftime("%Y-%m-%d"),
            "last_update_date": random.choice(last_update_dates).strftime("%Y-%m-%d"),
            "Focus_Details": generate_focus_details()
        }
        alert_data_list.append(alert_data)

    return alert_data_list

# Example usage:
branch_ids_example = load_branch_data('./OutputFiles/Branch.json')  # Update the path
alert_data_list_example = generate_alert_data(1000, branch_ids_example)

# Write data to JSON file
json_file_path = './OutputFiles/Alert.json'
with open(json_file_path, 'w') as jsonfile:
    json.dump(alert_data_list_example, jsonfile, indent=2)


# Write data to CSV file
# def write_to_csv(data_list, file_name):
#     with open(file_name, 'w', newline='') as csvfile:
#         fieldnames = data_list[0].keys()
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for row in data_list:
#             writer.writerow(row)

# write_to_csv(alert_data_list_example, '../OutputFiles/Alert.csv')  # Update the path
