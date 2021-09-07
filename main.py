import random

generatorotp = random.randint(000000,100000)
username = input("Username: ")

print("Hello User,enter: ")
print("Here is your otp for login please collect",generatorotp)
password = input("Enter the otp to login: ")

if password == str(generatorotp):
    print("Login Succes")
else:
    password != str(generatorotp)
    print("Login Failed")