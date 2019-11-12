import sys

# Constants
MASTER_PASSWORD = 'opensesame'

# in this form anyone can see the super secret pasword
password = input("Please enter the super secret password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town!")