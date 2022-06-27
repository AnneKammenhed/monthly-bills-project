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
    from user
    """
    
    print(f"Welcome to enter Your monthly bills!\n")

    rent_str = input("Enter cost for rent here:")
    employees_str = input("Enter the number of employees here:")
    telephone_str = input("Enter cost for telephone here:")
    print(f"The rent for this month is {rent_str}, the number of employees is {employees_str} and the telephone bills are {telephone_str}.\n")

collect_data()

# check if data is valid print error if not and return to beginning

# add function to multiply number of employees * 40000 for salary

# add rent, salary, telephone to worksheet

# calculate sum

# add sum to worksheet

# return sum to user

# calculate six month average

# return average to user