import numpy as np


# Function to calculate modular inverse
# This function finds the modular inverse of 'a' under modulo 'm'
def mod_inverse(a, m):
    a = a % m  # Ensure 'a' is within the range of modulo 'm'
    for x in range(1, m):
        if (a * x) % m == 1:  # Check if the modular inverse condition is satisfied
            return x
    return -1  # Return -1 if no modular inverse exists


# Function to encrypt a message using the Hill cipher
def hill_encrypt(key, message):
    size = len(key)  # Size of the key matrix
    message = message.lower().replace(" ", "")  # Convert message to lowercase and remove spaces
    while len(message) % size != 0:  # Pad the message with 'x' to make its length a multiple of the key size
        message += 'x'

    encrypted_message = ""
    for i in range(0, len(message), size):  # Process the message in blocks of 'size'
        block = [ord(char) - ord('a') for char in message[i:i + size]]  # Convert characters to numerical values
        encrypted_block = np.dot(key, block) % 26  # Perform matrix multiplication and take modulo 26
        encrypted_message += ''.join(chr(num + ord('a')) for num in encrypted_block)  # Convert back to characters

    return encrypted_message


# Function to decrypt a message using the Hill cipher
def hill_decrypt(key, encrypted_message):
    size = len(key)  # Size of the key matrix
    det = int(round(np.linalg.det(key))) % 26  # Calculate the determinant of the key matrix modulo 26
    det_inv = mod_inverse(det, 26)  # Find the modular inverse of the determinant
    if det_inv == -1:  # If no modular inverse exists, raise an error
        raise ValueError("Key matrix is not invertible under modulo 26.")

    # Calculate the adjugate matrix and the inverse key matrix modulo 26
    adjugate = np.round(det * np.linalg.inv(key)).astype(int) % 26
    inverse_key = (det_inv * adjugate) % 26

    decrypted_message = ""
    for i in range(0, len(encrypted_message), size):  # Process the encrypted message in blocks of 'size'
        block = [ord(char) - ord('a') for char in
                 encrypted_message[i:i + size]]  # Convert characters to numerical values
        decrypted_block = np.dot(inverse_key, block) % 26  # Perform matrix multiplication and take modulo 26
        decrypted_message += ''.join(chr(num + ord('a')) for num in decrypted_block)  # Convert back to characters

    return decrypted_message


# Main function to handle user input and perform encryption and decryption
def main():
    # Input the size of the key matrix
    size = int(input("Enter key matrix size (e.g., 2 for 2x2, 3 for 3x3): "))
    print(f"Enter the {size}x{size} key matrix:")

    # Input the key matrix
    key = []
    for _ in range(size):
        row = list(map(int, input().split()))  # Input each row of the key matrix
        key.append(row)
    key = np.array(key)  # Convert the key matrix to a NumPy array

    # Input the message to encrypt
    message = input("Enter the message to encrypt: ")
    encrypted_message = hill_encrypt(key, message)  # Encrypt the message
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the encrypted message
    decrypted_message = hill_decrypt(key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()