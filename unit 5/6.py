from importlib import import_module
import sys

try:
    _fernet = import_module("cryptography.fernet")
except ImportError:
    sys.exit(
        "The 'cryptography' package is required. Install it with: "
        "python -m pip install cryptography"
    )

Fernet = _fernet.Fernet
InvalidToken = _fernet.InvalidToken

# 1. Create a file with confidential text
with open("confidential.txt", "w") as file:
    file.write("This is confidential student information.")

print("Confidential file created successfully.")

# 2. Read the plaintext
with open("confidential.txt", "rb") as file:
    plaintext = file.read()

print("Plaintext:", plaintext.decode())

# 3, 4. Generate and save an encryption key
key = Fernet.generate_key()

with open("secret.key", "wb") as file:
    file.write(key)

cipher = Fernet(key)

# 5. Encrypt contents to a separate file
ciphertext = cipher.encrypt(plaintext)

with open("encrypted.bin", "wb") as file:
    file.write(ciphertext)

print("File encrypted successfully.")
print("Ciphertext:", ciphertext.decode())

# 6. Decrypt using the correct key
with open("encrypted.bin", "rb") as file:
    encrypted_data = file.read()

with open("secret.key", "rb") as file:
    correct_key = file.read()

try:
    decrypted_data = Fernet(correct_key).decrypt(encrypted_data)
    with open("decrypted.txt", "wb") as file:
        file.write(decrypted_data)

    print("Decryption successful!")
    print("Decrypted text:", decrypted_data.decode())

except InvalidToken:
    print("Decryption failed: Invalid key or corrupted data.")

# 7. Demonstrate an incorrect key
wrong_key = Fernet.generate_key()

try:
    Fernet(wrong_key).decrypt(encrypted_data)
    print("Decryption successful.")
except InvalidToken:
    print("Incorrect key: Decryption failed.")
