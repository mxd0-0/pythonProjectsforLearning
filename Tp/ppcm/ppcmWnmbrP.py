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

def ppcm_sans_pgcd(a, b):
    factors_a = Counter(prime_factors(a))
    factors_b = Counter(prime_factors(b))
    lcm_factors = factors_a & factors_b
    lcm = 1
    for factor in lcm_factors:
        lcm *= factor ** lcm_factors[factor]
    return lcm

def main():
    a = int(input("Entrez le premier nombre pair: "))
    b = int(input("Entrez le deuxième nombre pair: "))

    if a % 2 != 0 or b % 2 != 0:
        print("Veuillez entrer des nombres pairs uniquement.")
        return

    ppcm = ppcm_sans_pgcd(a, b)

    print(f"PPCM de {a} et {b} sans utiliser la méthode PGCD: {ppcm}")

if __name__ == "__main__":
    main()