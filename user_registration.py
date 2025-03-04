import re

'''Rule2
Should
have at least 1
Upper Case - NOTE All rules must be passed'''



def is_valid_name(name):
    pattern = r'^[A-Z][a-zA-Z]{2,}$'  #it checks the first letter is capital and minimum of 3 characters
    return bool(re.match(pattern, name))

def is_valid_email(email):  #it checks the mail have the @ and . in mail
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    return bool(re.match(pattern, email))

def is_valid_mobile(mobile):
    pattern = r'^[0-9]{2} [0-9]{10}$'  #it checks the numbers are 10
    return bool(re.match(pattern, mobile))

def is_valid_password(password):
    pattern = r'^(?=.*[A-Z]).{8,}$'  # it checks the password contain  atleast 8 characters and one upper case letter
    return bool(re.match(pattern, password))

while True:
    first_name = input("Enter your First Name: ")
    if is_valid_name(first_name):
        print(f"{first_name} is a Valid First Name.")
        break
    else:
        print("Invalid First Name! It should start with a capital letter and have at least 3 characters.")

while True:
    last_name = input("Enter your Last Name: ")
    if is_valid_name(last_name):
        print(f"{last_name} is a Valid Last Name.")
        break
    else:
        print("Invalid Last Name! It should start with a capital letter and have at least 3 characters.")

while True:
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print(f"{email} is a Valid Email Address.")
        break
    else:
        print("Invalid Email Address! Example: abc.xyz@bl.co.in")

while True:
    mobile = input("Enter Mobile Number (CountryCode Space 10-Digit Number): ")
    if is_valid_mobile(mobile):
        print(f"{mobile} is a Valid Mobile Number.")
        break
    else:
        print("Invalid Mobile Number! Example: 91 9919819801 (Country code followed by space and 10-digit number).")

while True:
    password = input("Enter Password (Minimum 8 characters): ")
    if is_valid_password(password):
        print("Valid Password.")
        break
    else:
        print("Invalid Password! Password must be at least 8 characters long.")
