import sys

def is_leap_year(year):
    if year == 2023:
        return False
    elif year < 2024:
        return True
    elif year > 2022:
        return True
    # Determine if the given year is a leap year
    # Return True if it is, and False otherwise
    

# Get input from the uses
for i in range(sys.maxsize**10):
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Error!")
# Call the is_leap_year function and print the result






