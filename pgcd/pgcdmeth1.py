def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def gcd_division(a, b):
    while b:
        a, b = b, a % b
    return a

from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def gcd_prime_factors(a, b):
    factors_a = Counter(prime_factors(a))
    factors_b = Counter(prime_factors(b))
    common_factors = factors_a & factors_b  # Intersection of the two counters, taking the min of each prime's count
    gcd = 1
    for factor in common_factors:
        gcd *= factor ** common_factors[factor]
    return gcd



def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    gcd1 = gcd_subtraction(a, b)
    gcd2 = gcd_division(a, b)
    gcd3 = gcd_prime_factors(a, b)

    print(f"GCD of {a} and {b} using Subtraction Method: {gcd1}")
    print(f"GCD of {a} and {b} using Division Method: {gcd2}")
    print(f"GCD of {a} and {b} using Prime Factorization Method: {gcd3}")

if __name__ == "__main__":
    main()