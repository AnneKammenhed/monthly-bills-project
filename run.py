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
    print(f"Welcome! Enter Your monthly bills!\n")

    rent_str = int(input("Enter cost for rent:"))
    rent_data = rent_str
    validate_rent_data(rent_data)

    employee_str = int(input("Enter number of employees:"))
    employee_data = employee_str*40000
    validate_employee_data(employee_str, employee_data)
    
    phone_str = int(input("Enter cost for phone bill:"))
    phone_data = phone_str
    validate_phone_data(phone_data)
    
def validate_rent_data(rent_data):
    """
    Function to validate that the data for monthly bills for rent. Print error if not and return to the beginning.

    """
    if rent_data <= 1000:
        print("Too few numbers. Add a few more!")
    else:
        print(f"You wrote {rent_data}. Thank you.")

def validate_employee_data(employee_str, employee_data):
    if employee_data >= 1000000:
        print(f"Impossible! With the answer {employee_str}, the cost would be {employee_data} and it is over your budget. Try again")
    else:
        print(f"You answered {employee_str}. With a monthly salary of 40000 SEK, the cost is {employee_data}")


def validate_phone_data(phone_data):
    """
    Function to validate that the data for monthly bills for rent. Print error if not and return to the beginning.

    """
    if phone_data <= 100:
        print("Too few numbers. Add a few more!")
    else:
        print(f"You wrote {phone_data}. Thank you.")

def update_bills_worksheet(data):
    """
    add rent, salary, telephone to worksheet
    """
    print("Updating worksheet with the bills for this month.....")
    bills_worksheet = SHEET.worksheet("bills")
    bills_worksheet.append_row(data)
    print("This months bills have been updated.")

# calculate sum

# add sum to worksheet

# return sum to user

# calculate six month average

# return average to user

#remember to call the functions here:

collect_data()
