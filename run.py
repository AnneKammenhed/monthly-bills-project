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
    Function to collect data about monthly bills for 
    rent and telephone. It also collects number of employees.
    from user and returns this number times the salary. All inputs has to be integers.
    """
    
    print(f"Welcome to enter Your monthly bills!\n")

    rent_str = int(input("Enter cost for rent:"))
    employees_str = int(input("Enter the number of employees:"))
    telephone_str = int(input("Enter cost for telephone:"))
    
    cost_data = [rent_str, employees_str*40000, telephone_str]
    validate_data(cost_data)

def validate_data(values):
    """
    Function to validate that all the the data for monthly bills for rent telephone and 
    employees are given. 
    """
    print(values)

    try:
        if len(values) == "":
            raise ValueError(
                f"You need to fill in all three values and you provided {len(values)}."
            )
    except ValueError as e:
        print(f"Invalid data {e}, please try again with integers.")

collect_data()

# check if data is valid print error if not and return to beginning

# add function to multiply number of employees * 40000 for salary

# add rent, salary, telephone to worksheet

# calculate sum

# add sum to worksheet

# return sum to user

# calculate six month average

# return average to user