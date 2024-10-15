def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is: {factorial(number)}")