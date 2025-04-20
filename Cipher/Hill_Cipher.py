import numpy as np
from sympy import Matrix
import string


class HillCipher:
    def __init__(self, matrix_size=3):
        """Initialize the Hill cipher with the specified matrix size (3x3 or 4x4)"""
        if matrix_size not in [3, 4]:
            raise ValueError("Matrix size must be either 3 or 4")
        self.matrix_size = matrix_size
        self.alphabet = string.ascii_lowercase
        self.mod = len(self.alphabet)  # 26

    def generate_key_matrix(self):
        """Generate a random invertible key matrix of the specified size"""
        while True:
            # Generate a random matrix with values between 0 and 25
            key_matrix = np.random.randint(0, self.mod, (self.matrix_size, self.matrix_size))

            # Check if the matrix is invertible in mod 26
            det = int(round(np.linalg.det(key_matrix))) % self.mod
            if np.gcd(det, self.mod) == 1:
                return key_matrix

    def set_key_matrix(self, key_matrix):
        """Set a custom key matrix"""
        if key_matrix.shape != (self.matrix_size, self.matrix_size):
            raise ValueError(f"Key matrix must be {self.matrix_size}x{self.matrix_size}")

        # Check if the matrix is invertible in mod 26
        det = int(round(np.linalg.det(key_matrix))) % self.mod
        if np.gcd(det, self.mod) != 1:
            raise ValueError("Matrix is not invertible in mod 26")

        self.key_matrix = key_matrix

    def text_to_vectors(self, text):
        """Convert text to numerical vectors"""
        # Remove non-alphabetic characters and convert to lowercase
        text = ''.join(filter(str.isalpha, text.lower()))

        # Pad the text if necessary
        pad_length = self.matrix_size - (len(text) % self.matrix_size)
        if pad_length < self.matrix_size:
            text += 'x' * pad_length

        # Convert text to numerical values
        numeric_text = [self.alphabet.index(char) for char in text]

        # Split into vectors of size matrix_size
        vectors = [numeric_text[i:i + self.matrix_size] for i in range(0, len(numeric_text), self.matrix_size)]

        return vectors

    def vectors_to_text(self, vectors):
        """Convert numerical vectors back to text"""
        text = ""
        for vector in vectors:
            for num in vector:
                text += self.alphabet[num]
        return text

    def encrypt(self, plaintext):
        """Encrypt plaintext using the Hill cipher"""
        vectors = self.text_to_vectors(plaintext)
        encrypted_vectors = []

        for vector in vectors:
            # Perform matrix multiplication and modulo
            result = np.dot(self.key_matrix, vector) % self.mod
            encrypted_vectors.append(result.tolist())

        return self.vectors_to_text(encrypted_vectors)

    def calculate_inverse_matrix(self):
        """Calculate the inverse of the key matrix in mod 26"""
        # Convert to SymPy matrix for modular arithmetic
        sympy_matrix = Matrix(self.key_matrix)

        # Calculate modular multiplicative inverse
        inverse_matrix = sympy_matrix.inv_mod(self.mod)

        # Convert back to numpy array
        return np.array(inverse_matrix.tolist(), dtype=int)

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using the Hill cipher"""
        vectors = self.text_to_vectors(ciphertext)
        inverse_matrix = self.calculate_inverse_matrix()
        decrypted_vectors = []

        for vector in vectors:
            # Perform matrix multiplication with the inverse matrix and modulo
            result = np.dot(inverse_matrix, vector) % self.mod
            decrypted_vectors.append(result.tolist())

        return self.vectors_to_text(decrypted_vectors)


# Example usage for 3x3 matrix
def demo_3x3():
    print("\n=== Hill Cipher 3x3 Demo ===")
    hill_cipher = HillCipher(matrix_size=3)

    # Set a specific key matrix (must be invertible in mod 26)
    key_matrix_3x3 = np.array([
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ])
    hill_cipher.set_key_matrix(key_matrix_3x3)

    print(f"Key Matrix (3x3):\n{hill_cipher.key_matrix}")

    plaintext = "thequickbrownfoxjumpsoverthelazydog"
    print(f"\nOriginal text: {plaintext}")

    encrypted = hill_cipher.encrypt(plaintext)
    print(f"Encrypted text: {encrypted}")

    decrypted = hill_cipher.decrypt(encrypted)
    print(f"Decrypted text: {decrypted}")


# Example usage for 4x4 matrix
def demo_4x4():
    print("\n=== Hill Cipher 4x4 Demo ===")
    hill_cipher = HillCipher(matrix_size=4)

    # Set a specific key matrix (must be invertible in mod 26)
    key_matrix_4x4 = np.array([
        [9, 7, 11, 13],
        [4, 7, 5, 6],
        [2, 21, 14, 9],
        [3, 23, 21, 8]
    ])
    hill_cipher.set_key_matrix(key_matrix_4x4)

    print(f"Key Matrix (4x4):\n{hill_cipher.key_matrix}")

    plaintext = "thequickbrownfoxjumpsoverthelazydog"
    print(f"\nOriginal text: {plaintext}")

    encrypted = hill_cipher.encrypt(plaintext)
    print(f"Encrypted text: {encrypted}")

    decrypted = hill_cipher.decrypt(encrypted)
    print(f"Decrypted text: {decrypted}")


# Run the demos
if __name__ == "__main__":
    demo_3x3()
    demo_4x4()