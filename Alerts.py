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
    focus_types = ["Mutual Fund Short-Term Liquidation", "Suspicious Trading Activity"]
    focus_names = ["Mutual Fund Short-Term Liquidation", "Suspicious Trading Activity"]
    focus_descriptions = ["An early liquidation of a mutual fund has occurred outside the guidelines.", "Unusual trading patterns or transactions suggesting potential market abuse, manipulation, or insider trading, deviating from standard market practices"]
    
    focus_details = []
    for focus_type, focus_name, focus_description in zip(focus_types, focus_names, focus_descriptions):
        scenarios = []
        if focus_type == "Mutual Fund Short-Term Liquidation":
            scenarios = [
                {
                    "Scenario_Id": "SC001",
                    "Scenario_Name": "Mutual Fund Short-Term Liquidation - Share Class B",
                    "Scenario_Description": "An early liquidation of a mutual fund has occurred and the client has incurred a CDSC",
                    "Threshold_Value": 80,
                    "Actual_Value": 90,
                    "Score": 100
                },
                {
                    "Scenario_Id": "SC002",
                    "Scenario_Name": "Mutual Fund Short-Term Liquidation - Share Class C",
                    "Scenario_Description": "An early liquidation of a mutual fund has occurred in C shares and the client has incurred a CDSC",
                    "Threshold_Value": 80,
                    "Actual_Value": 90,
                    "Score": 100
                }
            ]
        elif focus_type == "Suspicious Trading Activity":
            scenarios = [
                {
                    "Scenario_Id": "SC004",
                    "Scenario_Name": "Abnormal Price Movements",
                    "Scenario_Description": "Sudden and significant price movements in a security with no apparent news or fundamental reason, potentially indicating market manipulation or insider trading.",
                    "Threshold_Value": 10,
                    "Actual_Value": 8,
                    "Score": 80
                },
                {
                    "Scenario_Id": "SC005",
                    "Scenario_Name": "Front-Running",
                    "Scenario_Description": "A trader executes orders on a security based on advanced knowledge of pending trades from a client, typically to benefit from the anticipated price movement, which is illegal and unethical.",
                    "Threshold_Value": 4,
                    "Actual_Value": 3,
                    "Score": 70
                },
                {
                    "Scenario_Id": "SC006",
                    "Scenario_Name": "Insider Trading",
                    "Scenario_Description": "Trading in a security based on material, non-public information about the security, in violation of securities laws.",
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
    alert_types = ["Trade_Review"]
    status_ids = ["Ready for Analysis", "In Progress", "Confirmed", "False Positive", "Closed", "Escalated", "Under Review", "Pending"]
    business_units = branch_ids
    business_unit_families = ["[Firm:US:East Regon:Branch1]", "[Firm:US:West Regon:Branch2]", "[Firm:US:South Regon:Branch3]"]
    business_unit_families_previous = ["[Firm:US:East Regon:Branch1]", "[Firm:US:West Regon:Branch2]", "[Firm:US:South Regon:Branch3]"]
    details = ["Mutual Fund liquidated by client ABC before maturity. ", "Client XYZ has performed Suspicious Trading Activity"]
    states = ["Ready for Analysis", "In Progress", "Confirmed", "False Positive", "Closed", "Escalated", "Under Review", "Pending"]
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
            "score": round(random.uniform(0, 100), 0),
            "state": random.choice(states),
            "business_date": random.choice(business_dates).strftime("%Y-%m-%d"),
            "create_date": random.choice(create_dates).strftime("%Y-%m-%d"),
            "last_update_date": random.choice(last_update_dates).strftime("%Y-%m-%d"),
            "Focus_Details": generate_focus_details(),
            "Custom_Fields": "{\"extra_fields\":{\"Is_Centralized\":true,\"Is_Whitelist\":false,\"Customer_Info\":{\"Customer_Id\":\"C123\",\"Name\":\"John Doe\",\"Address\":\"123 Main St\",\"City\":\"New York\",\"State\":\"NY\",\"Zip\":\"10001\",\"Phone_Number\":\"555-123-4567\",\"Email\":\"john.doe@example.com\",\"Date_of_Birth\":\"1970-01-01\",\"Nationality\":\"American\"},\"Account_Suitability_Info\":{\"Account_Type\":\"Checking\",\"Risk_Tolerance\":\"Medium\",\"Investment_Goals\":\"Retirement\",\"Investment_Time_Horizon\":\"Long-term\",\"Investment Strategy\":\"Aggressive Growth\"},\"Account_Information\":{\"Account_Number\":\"987654321\",\"Account_Opened_Date\":\"2022-01-01\",\"Account_Balance\":100000.00,\"State\":\"California\",\"Branch\":\"Los Angeles\"},\"Trade_Information\":{\"Trade_ID\":\"TRADE123\",\"Trade_Date\":\"2024-03-24\",\"Trade_Execution_Date\":\"2024-03-24\",\"Trade_Type\":\"Buy\",\"Symbol\":\"AAPL\",\"Quantity\":100,\"Price\":150.00,\"Total_Amount\":15000.00,\"Trade_Status\":\"Executed\",\"Direction\":\"In\",\"Order_ID\":\"ORDER456\",\"Order_Date\":\"2024-03-24\",\"Order_Placed_By\":\"John Doe\",\"Is_Solicited\":true,\"Is_Descriptive\":false,\"Product_Name\":\"Apple Inc.\",\"Product_Symbol\":\"AAPL\",\"CUSIP\":\"037833100\",\"Commission\":10.00,\"Fee\":5.00,\"Focal_Entity\":\"ABC Corp\",\"Focus\":\"Growth\",\"Advisor_Id\":\"AD123\",\"Advisor_Name\":\"Jane Smith\"},\"Advisor_Information\":{\"Advisor_Id\":\"AD123\",\"Advisor_Name\":\"Jane Smith\"}}}"
        }
        alert_data_list.append(alert_data)

    return alert_data_list

# Example usage:
branch_ids_example = load_branch_data('./OutputFiles/Branch.json')  # Update the path
alert_data_list_example = generate_alert_data(100, branch_ids_example)

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
