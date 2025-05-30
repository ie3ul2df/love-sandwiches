import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
CREDS_SCOPED = CREDS.with_scopes(SCOPE)
GSPRED_CLIENT = gspread.authorize(CREDS_SCOPED)
SHEET = GSPRED_CLIENT.open("love_sandwiches")

# sales = SHEET.worksheet("sales")
# data = sales.get_all_values()

# print(data)

def get_sales_data():
    """
    Get sales data from the sales worksheet.
    Returns a list of lists containing the sales data.
    """
    print("\n")
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    # print(f"You entered: {data_str}\n")
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """    
    Validate the input data.
    Raise ValueError if the data is invalid. 
    """
    try:
        [int(value) for value in values]  # Convert all values to integers
        if len(values) != 6:
            raise ValueError(
                f"Exactly six values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    


get_sales_data()