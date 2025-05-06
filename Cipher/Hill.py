import math
import numpy as np

def get_matrix_size(key: str) -> int:
    n = int(math.sqrt(len(key)))
    if n * n != len(key):
        raise ValueError("Key length must be a perfect square.")
    return n

def get_key_matrix(key: str, n: int) -> np.ndarray:
    return np.array([[(ord(key[i * n + j]) % 65) for j in range(n)] for i in range(n)])

def get_message_vector(message: str) -> np.ndarray:
    return np.array([[ord(char) % 65] for char in message])

def mod_inv(a, m):
    """Return modular inverse of a under mod m, if it exists."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under mod {m}")

def matrix_mod_inv(matrix, modulus):
    """Find modular inverse of a matrix under modulus."""
    det = int(round(np.linalg.det(matrix))) % modulus
    det_inv = mod_inv(det, modulus)

    matrix_minor = np.linalg.inv(matrix) * det
    adjugate = np.round(matrix_minor).astype(int) % modulus

    return (det_inv * adjugate) % modulus

def encrypt(message, key_matrix, n):
    message_vector = get_message_vector(message)
    cipher_vector = np.dot(key_matrix, message_vector) % 26
    return ''.join(chr(int(val[0]) + 65) for val in cipher_vector)

def decrypt(ciphertext, key_matrix, n):
    try:
        inverse_key = matrix_mod_inv(key_matrix, 26)
    except ValueError as e:
        print("Decryption failed:", e)
        return None

    cipher_vector = get_message_vector(ciphertext)
    message_vector = np.dot(inverse_key, cipher_vector) % 26
    return ''.join(chr(int(val[0]) + 65) for val in message_vector)

def get_user_input():
    while True:
        try:
            key = input("Enter key (perfect square length): ").strip().upper()
            n = get_matrix_size(key)
            message = input(f"Enter message (exactly {n} letters): ").strip().upper()
            if len(message) != n:
                print(f"Message must be exactly {n} characters.")
                continue
            return message, key, n
        except ValueError as e:
            print("Error:", e)

def main():
    print("=== Hill Cipher (Encrypt + Decrypt) ===")
    message, key, n = get_user_input()
    key_matrix = get_key_matrix(key, n)

    print("\nEncrypting...")
    cipher = encrypt(message, key_matrix, n)
    print("Ciphertext:", cipher)

    print("\nDecrypting...")
    plain = decrypt(cipher, key_matrix, n)
    if plain:
        print("Decrypted text:", plain)

if __name__ == "__main__":
    main()
