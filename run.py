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
    
    while True:
        print(f"Welcome! Enter Your monthly bills!\n")

        rent_str = input("Enter cost for rent:")
        employees_str = input("Enter the number of employees:")
        telephone_str = input("Enter cost for telephone:")
    
        cost_data = rent_str + employees_str + telephone_str
        
        if validate_data(cost_data):
            print("Data is valid")
            break

    return cost_data
        
def validate_data(values):
    """
    Function to validate that all the the data for monthly bills for rent telephone and 
    employees are given. Print error if not and return to the beginning.

    """
   
    try:
        [int(value)for value in values]
        if len(values) != 3:
            raise ValueError(
                f"You need to fill in all 3 values and you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data {e}, please try again with integers.")
        return False
    
    return True


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

data = collect_data()
cost_data = [int(num) for num in data]
update_bills_worksheet(cost_data)