import re

def is_valid_first_name(name):
    pattern = r'^[A-Z][a-zA-Z]{2,}$'  
    return bool(re.match(pattern, name))

while True:
    first_name = input("Enter your First Name: ")
    if is_valid_first_name(first_name):
        print(f"{first_name} is a Valid First Name.")
        break
    else:
        print("Invalid First Name! It should start with a capital letter and have at least 3 characters.")
