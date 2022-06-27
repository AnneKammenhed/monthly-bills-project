# google api info
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("monthly_bills")


def collect_data():
    """
    Function to collect data about bills for 
    rent and telephone from user. Also number of eoployees.
    """
    
    print(f"Welcome to Annes monthly cost calculator!")

collect_data()
bills = SHEET.worksheet("bills")
data = bills.get_all_values()
print(data)

# check if data is valid print error if not and return to beginning

# add function to multiply number of employees * 40000 for salary

# add rent, salary, telephone to worksheet

# calculate sum

# add sum to worksheet

# return sum to user

# calculate six month average

# return average to user