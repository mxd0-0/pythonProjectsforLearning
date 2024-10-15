def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter the number of Fibonacci numbers to print: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The first {n} numbers of the Fibonacci sequence are: {fibonacci(n)}")