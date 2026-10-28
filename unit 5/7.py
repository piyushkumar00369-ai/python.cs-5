
import os
import json
import base64
import hashlib
import hmac
from cryptography.fernet import Fernet

# File names
USER = "users.json"
KEY = "secret.key"
DATA = "protected_data.enc"

# Password hashing
def hash_password(password, salt):
    return hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)

# Create or load encryption key
if not os.path.exists(KEY):
    with open(KEY, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY, "rb") as f:
    cipher = Fernet(f.read())

# Create account on first run
if not os.path.exists(USER):
    username = input("Create username: ")
    password = input("Create password: ")
    salt = os.urandom(16)

    user = {
        "username": username,
        "salt": base64.b64encode(salt).decode(),
        "password_hash": base64.b64encode(
            hash_password(password, salt)
        ).decode()
    }

    with open(USER, "w") as f:
        json.dump(user, f)

    print("Account created!")
else:
    with open(USER, "r") as f:
        user = json.load(f)

    username = input("Username: ")
    password = input("Password: ")
    salt = base64.b64decode(user["salt"])

    entered_hash = hash_password(password, salt)
    saved_hash = base64.b64decode(user["password_hash"])

    if username != user["username"] or not hmac.compare_digest(
        entered_hash, saved_hash
    ):
        print("Login failed!")
        raise SystemExit

    print("Login successful!")

# Create encrypted file
if not os.path.exists(DATA):
    with open(DATA, "wb") as f:
        f.write(cipher.encrypt(b"Confidential information\n"))

# Menu
while True:
    print("\n1. Read file")
    print("2. Add data")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        with open(DATA, "rb") as f:
            print(cipher.decrypt(f.read()).decode())

    elif choice == "2":
        with open(DATA, "rb") as f:
            content = cipher.decrypt(f.read())

        new_text = input("Enter text: ")
        with open(DATA, "wb") as f:
            f.write(cipher.encrypt(content + (new_text + "\n").encode()))

        print("Data saved securely!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
