import random
import time
txt = "PASSWORD GENERATOR"
cent = txt.center(130)
time.sleep(1)

print("\n",cent)

no_of_password = int(input("Enter how many variations of password you want: "))
time.sleep(0.5)
password_length = int(input("enter the length of password: "))

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$&!*"

print("\nList of your passwords:")

for i in range(no_of_password):
    password = ''
    for j in range(password_length):
        password += random.choice(chars)
    print(password)
