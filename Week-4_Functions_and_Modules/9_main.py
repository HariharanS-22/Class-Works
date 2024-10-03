import re

email = input("Enter an email id : ")
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, email):
    print("The given email address is valid")
else:
    print("The given email address is not valid")
