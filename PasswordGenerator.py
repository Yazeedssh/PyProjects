import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the password generator")

NOL = int(input("How many ltters do you want in your password? "))
NON = int(input("How many numbers do you want in your password? "))
NOS = int(input("How many symbols do you want in your password? "))

password_list = []

for l in range(1, NOL + 1):
    password_list += random.choice(letters)

for n in range(1, NON + 1):
    password_list += random.choice(numbers)

for s in range(1, NOS + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(password)
