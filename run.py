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
    print(f"You entered: {data_str}\n")

get_sales_data()