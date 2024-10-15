from random import random


def intgerGenerator():
    return int(random() * 100)


print("If you are ready, tap enter")
b = input()
print("Guess the number between 1 to 100")
c = int(input())
a = intgerGenerator()
while a != c:
    if a > c:
        print("Your number is smaller")
        c = int(input())
        if a == c:
            print("You got it")
    else:
        print("Your number is bigger")
        c = int(input())
