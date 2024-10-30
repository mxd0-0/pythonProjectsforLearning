import math

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def ppcm_avec_pgcd(a, b):
    return abs(a * b) // pgcd(a, b)

def main():
    a = int(input("Entrez le premier nombre: "))
    b = int(input("Entrez le deuxième nombre: "))

    ppcm = ppcm_avec_pgcd(a, b)

    print(f"PPCM de {a} et {b} en utilisant la méthode PGCD: {ppcm}")

if __name__ == "__main__":
    main()