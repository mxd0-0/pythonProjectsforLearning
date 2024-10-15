import random


def passwordGenerator(length=12):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?"
    password = ''.join(random.choice(char) for _ in range(length))
    return password
print("give the length of your password: ")
b= int(input())
print("how many password you want?")
c= int(input())
for i in range(c):
    print(passwordGenerator(b))



