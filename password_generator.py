import random

print("===== PASSWORD GENERATOR =====")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)

if length < 6:
    print("Password Strength: Weak")
elif length < 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

input("\nPress Enter to exit...")
