import csv
import json
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Load client data from the Client.json file
def load_client_data(file_name):
    with open(file_name, 'r') as jsonfile:
        client_data = json.load(jsonfile)
    return [client["ClientID"] for client in client_data]

# Function to generate unique account IDs
def generate_unique_account_ids(min_account_id, max_account_id, num_ids):
    return random.sample(range(min_account_id, max_account_id + 1), num_ids)

# Function to generate random 12-digit unique account number
def generate_account_number(used_account_numbers):
    while True:
        account_number = str(fake.uuid4())[:11].upper().replace('-', '') #''.join(random.choices('0123456789', k=12))
        if account_number not in used_account_numbers:
            used_account_numbers.add(account_number)
            return account_number

# Function to generate random date within a given range
def random_date(start_date, end_date):
    return fake.date_time_between_dates(datetime_start=start_date, datetime_end=end_date)

# Function to generate mock data for the Account table
def generate_account_data(client_ids, num_of_rows=1000):
    account_types = [
        "Cash Account", "Margin Account", "Trading Account", "Retirement Account (e.g., IRA)",
        "Joint Account", "Corporate Account", "Trust Account", "Managed Account", "Savings Account",
        "Custodial Account"
    ]

    account_statuses = ["Active", "Inactive", "Closed"]
    risk_tolerances = ["Conservative", "Moderate", "Aggressive", "Risk-Averse", "Risk-Seeking", "Balanced",
                       "Income-Oriented", "Speculative"]
    liquidity_needs = ["High Liquidity Needs", "Moderate Liquidity Needs", "Low Liquidity Needs",
                       "Flexible Liquidity", "Emergency Fund", "Immediate Cash Requirements", "Regular Cash Flow",
                       "No Immediate Liquidity Needs", "Strategic Cash Reserves", "Short-Term Expense Coverage",
                       "Opportunistic Liquidity", "Tailored Liquidity"]
    investment_experiences = ["Novice", "Beginner", "Intermediate", "Experienced", "Advanced", "Professional",
                              "Institutional", "No Experience", "Limited Experience", "Moderate Experience",
                              "Extensive Experience", "Risk-Averse Investor", "Speculative Trader", "Technical Analyst",
                              "Fundamental Analyst", "Active Trader", "Passive Investor", "Options Trader",
                              "Crypto Enthusiast", "Real Estate Investor", "Retirement Investor", "Wealth Manager"]
    tax_considerations = ["Tax-Deferred Accounts (e.g., 401(k), IRA)", "Taxable Accounts", "Capital Gains Tax",
                          "Dividend Tax", "Interest Income Tax", "Tax-Loss Harvesting", "Tax-Efficient Investing",
                          "Tax Credits", "Qualified Dividend Income", "Long-Term Capital Gains", "Short-Term Capital Gains",
                          "Tax Bracket", "Tax-Advantaged Investments", "Roth Conversions", "Estate Tax Planning",
                          "Gift Tax", "Alternative Minimum Tax (AMT)", "Tax Diversification", "Charitable Contributions",
                          "Section 1256 Contracts", "Wash Sale Rule", "Tax-Loss Carryforward", "529 Plans (Education Savings)",
                          "HSA (Health Savings Account)", "Tax-Exempt Bonds", "Depreciation (for Real Estate)",
                          "Tax Filing Status", "Foreign Tax Credits", "Self-Employment Tax"]
    asset_allocation_list = ["Equities (Stocks)", "Fixed-Income Securities (Bonds)", "Cash and Cash Equivalents",
                        "Real Estate Investment Trusts (REITs)", "Commodities", "Precious Metals (Gold, Silver)",
                        "Cryptocurrencies", "Foreign Exchange (Forex)", "Private Equity", "Hedge Funds",
                        "Derivatives (Options, Futures)", "Collectibles (Art, Antiques)", "Venture Capital",
                        "Government Bonds", "Municipal Bonds", "Corporate Bonds", "Money Market Instruments",
                        "Index Funds", "Exchange-Traded Funds (ETFs)", "Real Assets (Natural Resources)",
                        "Infrastructure Investments", "Certificates of Deposit (CDs)", "Savings Accounts",
                        "Treasury Securities", "Master Limited Partnerships (MLPs)", "Peer-to-Peer Lending",
                        "Structured Products", "Foreign Bonds", "Sovereign Wealth Funds"]

    # Set the range of unique account IDs
    min_account_id = 0
    max_account_id = 9999999999

    # Generate unique account IDs
    unique_account_ids = generate_unique_account_ids(min_account_id, max_account_id, num_of_rows)
    
    account_data_list = []
    used_account_numbers = set()

    for _ in range(num_of_rows):
        client_id = random.choice(client_ids)
        account_id = unique_account_ids.pop()
        #account_id = fake.uuid4()
        primary_client_id = client_id
        account_number = generate_account_number(used_account_numbers)
        account_type = random.choice(account_types)
        account_status = random.choice(account_statuses)
        currency = "USD"
        margin_level = ""
        trading_permission = "Yes"
        leverage = str(random.choice([0, 2, 3]))
        risk_tolerance = random.choice(risk_tolerances)
        open_date = random_date(datetime(2020, 1, 1), datetime(2024, 1, 1)).strftime("%Y-%m-%d")
        close_date = ""
        account_description = ""
        interest_rate = None
        dividend_option = None
        tax_status = "Taxable"
        trading_authority = "Self"
        is_fee_based_account = random.choice([1, 0])
        fee_percentage = round(random.uniform(0.01, 2.99), 2) if is_fee_based_account == 1 else None
        is_dvp_account = random.choice([1, 0])
        risk_profile = random.choice(risk_tolerances)
        investment_objective = random.choice([
            "Capital Preservation", "Income Generation", "Wealth Accumulation", "Risk Diversification",
            "Retirement Planning", "Education Funding", "Home Purchase", "Estate Planning", "Tax Efficiency",
            "Socially Responsible Investing", "Speculative Trading", "Short-Term Liquidity", "Entrepreneurial Ventures",
            "Emergency Fund", "Charitable Giving", "Real Estate Investment", "Business Expansion",
            "International Diversification", "Value Investing", "Dividend Growth", "Capital Appreciation"
        ])
        asset_allocation = random.choice(asset_allocation_list)
        liquidity_needs_list = random.choice(liquidity_needs)
        investment_experience = random.choice(investment_experiences)
        tax_considerations_list = random.choice(tax_considerations)
        is_managed_account = random.choice([1, 0])
        management_fee = round(random.uniform(0.01, 2.99), 2) if is_managed_account == 1 else None
        managed_strategy = random.choice([
            "Passive Investing", "Active Investing", "Income Generation", "Growth Investing", "Value Investing",
            "Dividend Growth", "Balanced Portfolio", "Risk Parity", "Tactical Asset Allocation",
            "Strategic Asset Allocation", "Sector Rotation", "Factor-Based Investing", "Quantitative Strategies",
            "Socially Responsible Investing (SRI)", "ESG (Environmental, Social, Governance) Investing",
            "Hedging Strategies", "Alternative Investments", "Global Diversification", "Market Timing",
            "Dollar-Cost Averaging", "Buy and Hold", "Robo-Advisory", "Systematic Trading", "Arbitrage Strategies",
            "Options Trading", "Fixed-Income Strategies", "Real Estate Investment", "Private Equity Exposure",
            "Currency Hedging"
        ])
        is_auto_investment_plan = 0
        auto_inv_model_id = ""
        is_institutional = 1 if account_type == "Corporate Account" else 0
        account_rep_primary = random.choice(["RM001", "RM002", "RM003", "RM004", "RM005"])
        account_branch_primary = random.choice(["Branch001", "Branch002", "Branch003", "Branch004", "Branch005"])
        is_bank_account = 1
        is_fx_allowed = 0
        is_option_allowed = random.choice([0, 1])
        is_commodity_allowed = random.choice([0, 1])
        is_trust_account = 1 if account_type == "Trust Account" else 0
        is_joint_account = 1 if account_type == "Joint Account" else 0
        is_commission_based = random.choice([0, 1])
        is_discretionary = 1 if is_managed_account == 1 else 0
        account_owner_id = ""
        is_leverage_etf_allowed = 1 if leverage != '0' else 0

        account_data = {
            "Account_ID": str(account_id),
            "Primary_client_id": str(primary_client_id),
            "Account_Number": account_number,
            "Account_Type": account_type,
            "Account_Status": account_status,
            "Currency": currency,
            "Margin_Level": margin_level,
            "Trading_Permission": trading_permission,
            "Leverage": leverage,
            "Risk_Tolerance": risk_tolerance,
            "Open_Date": open_date,
            "Close_Date": close_date,
            "Account_Description": account_description,
            "Interest_Rate": interest_rate,
            "Dividend_Option": dividend_option,
            "Tax_Status": tax_status,
            "Trading_Authority": trading_authority,
            "Is_Fee_Based_Account": is_fee_based_account,
            "Fee_Percentage": fee_percentage,
            "Is_DVP_Account": is_dvp_account,
            "Risk_Profile": risk_profile,
            "Investment_Objective": investment_objective,
            "Asset_Allocation": asset_allocation,
            "Liquidity_Needs": liquidity_needs_list,
            "Investment_Experience": investment_experience,
            "Tax_Considerations": tax_considerations_list,
            "Is_Managed_Account": is_managed_account,
            "Management_Fee": management_fee,
            "Managed_Strategy": managed_strategy,
            "Is_Auto_Investment_Plan": is_auto_investment_plan,
            "Auto_inv_model_id": auto_inv_model_id,
            "Is_Institutional": is_institutional,
            "Account_Rep_Primary": account_rep_primary,
            "Account_Branch_Primary": account_branch_primary,
            "Is_Bank_Account": is_bank_account,
            "Is_Fx_Allowed": is_fx_allowed,
            "Is_Option_Allowed": is_option_allowed,
            "Is_Commodity_Allowed": is_commodity_allowed,
            "Is_Trust_Account": is_trust_account,
            "Is_Joint_Account": is_joint_account,
            "Is_Commission_Based": is_commission_based,
            "Is_Discretionary": is_discretionary,
            "Account_Owner_id": account_owner_id,
            "Is_Leverage_ETF_Allowed": is_leverage_etf_allowed
        }

        account_data_list.append(account_data)

    return account_data_list

# Example usage:
client_ids_example = load_client_data('./OutputFiles/Client.json')  # Update the path
num_of_rows_per_client = 1000000
account_data_list_example = generate_account_data(client_ids_example, num_of_rows_per_client)

# Write data to CSV file
def write_to_csv(data_list, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = data_list[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)

# Write data to CSV file inside the "./OutputFiles/" directory
write_to_csv(account_data_list_example, './OutputFiles/Account.csv')  # Update the path

# Write data to JSON file
"""json_file_path = './OutputFiles/Account.json'
with open(json_file_path, 'w') as jsonfile:
    json.dump(account_data_list_example, jsonfile, indent=2)"""