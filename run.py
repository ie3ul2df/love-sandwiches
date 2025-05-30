import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    while True:
        print("\n")
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        # print(f"You entered: {data_str}\n")
        sales_data = data_str.split(",")
       
        if validate_data(sales_data):
            print(f"Data is valid: {sales_data}\n")
            break

    return sales_data


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
        return False
    
    return True
    

def update_sales_worksheet(data):
    """
    Update the sales worksheet with the provided data.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    Calculate surplus data based on sales and stock.
    Returns a list of surplus data.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    # pprint(stock)
    stock_row = stock[-1]
    # pprint(f"Stock row: {stock_row}\n")
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - int(sales)
        surplus_data.append(surplus)

    # pprint(f"Surplus data: {surplus_data}\n")
    return surplus_data

def update_surplus_worksheet(data):
    """
    Update the surplus worksheet with the provided data.
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully.\n")



def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    update_surplus_worksheet(new_surplus_data)

print("Welcome to Love Sandwiches Data Automation")
main()