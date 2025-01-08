import re

email_condition = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

input_email = input('Enter your email: ')

if re.search(email_condition,input_email):
    print(f'Valid Email, {input_email}')
else:
    print('Email is not valid')
