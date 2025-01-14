from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

# Input from the user
try:
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")
