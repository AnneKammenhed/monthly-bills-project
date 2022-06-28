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
    from user and returns this number times the salary. It also 
    validates that all input values are integers and returns standard message.
    """
    print(f"Welcome! Enter Your monthly bills!\n")

    while True:
        rent_str = int(input("Enter cost for rent:"))
        rent_data = rent_str

        if validate_rent_data(rent_data):
            break
    
    while True:
        employee_str = int(input("Enter number of employees:"))
        employee_data = employee_str*40000

        if validate_employee_data(employee_str, employee_data):
            break
    
    while True:
        phone_str = int(input("Enter cost for phone bill:"))
        phone_data = phone_str

        if validate_phone_data(phone_data):
            break

    return rent_data, employee_data, phone_data
    
def validate_rent_data(rent_data):
    """
    Function to validate that the data for monthly bills for rent i over 1000SEK. 
    Prints error if not and return to ask for rent .

    """
    try:
        if rent_data <= 1000:
            raise ValueError(
                f"You wrote {rent_data} SEK which is too cheap"
            )
        else:
            print(f"You wrote {rent_data} SEK. Thank you!")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again!")
        return False
    
    return True

def validate_employee_data(employee_str, employee_data):
    """
    Function to validate that the data for monthly bills for salary is over 1000000 SEK. 
    Print error if it is  and return to ask for number of employees.
    """
    try:
        if employee_data >= 1000000:
            raise ValueError(
                f"Impossible! With the answer {employee_str}, the cost would be {employee_data} SEK and it is over your budget"
            )
        else:
            print(f"You answered {employee_str} and the cost is {employee_data} SEK")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again!")
        return False
    
    return True

def validate_phone_data(phone_data):
    """
    Function to validate that the data for monthly bills for phone is over 100 SEK. 
    Print error if not and return to ask for phone cost.

    """
    try:
        if phone_data <= 100:
            raise ValueError(
                f"You answered {phone_data} SEK which is too little"
            )
        else:
            print(f"You wrote {phone_data} SEK. Thank you!")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again!")
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
