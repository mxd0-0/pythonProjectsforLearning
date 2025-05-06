import math

# Efficient Modular Exponentiation: (base^exp) % mod
def mod_exp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Extended Euclidean Algorithm to find modular inverse
def mod_inverse(e, phi):
    r1, r2 = phi, e
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        t1, t2 = t2, t1 - q * t2
    return t1 % phi if r1 == 1 else None

# GCD Function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Basic Prime Check
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Key Generation
def generate_keys():
    while True:
        try:
            p = int(input("🔢 Enter a prime number p: "))
            q = int(input("🔢 Enter a different prime number q: "))
            if not (is_prime(p) and is_prime(q)):
                raise ValueError("Both numbers must be prime.")
            if p == q:
                raise ValueError("p and q must be different.")
            break
        except ValueError as e:
            print(f"❌ {e}")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) == 1
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    else:
        raise Exception("Couldn't find valid 'e'.")

    d = mod_inverse(e, phi)
    if d is None:
        raise Exception("Modular inverse of e doesn't exist.")

    print(f"\n✅ Public Key:  (e={e}, n={n})")
    print(f"🔐 Private Key: (d={d}, n={n})")
    return e, d, n

# Encrypt Message
def encrypt(message, e, n):
    return mod_exp(message, e, n)

# Decrypt Message
def decrypt(ciphertext, d, n):
    return mod_exp(ciphertext, d, n)

# Main Function
def main():
    print("🔐 RSA Encryption/Decryption System")
    e, d, n = generate_keys()

    while True:
        try:
            message = int(input("\n✉️ Enter a message to encrypt (as integer < n): "))
            if message >= n:
                raise ValueError("Message must be less than n.")
            break
        except ValueError as ve:
            print(f"❌ {ve}")

    cipher = encrypt(message, e, n)
    print(f"🔒 Encrypted Message: {cipher}")

    original = decrypt(cipher, d, n)
    print(f"🔓 Decrypted Message: {original}")

if __name__ == "__main__":
    main()
