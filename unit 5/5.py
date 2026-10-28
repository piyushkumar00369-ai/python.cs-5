import hashlib
import hmac

DIGEST_FILE = "password-digest.txt"

sample_password = input("Create a sample password: ")
if not sample_password:
    print("Password cannot be empty.")
else:
    # Save the password's SHA-256 digest instead of the password itself.
    password_digest = hashlib.sha256(sample_password.encode("utf-8")).hexdigest()
    with open(DIGEST_FILE, "w", encoding="utf-8") as digest_file:
        digest_file.write(password_digest)

    print(f"Saved the password digest to {DIGEST_FILE}.")

    entered_password = input("Enter the password to verify: ")
    entered_digest = hashlib.sha256(entered_password.encode("utf-8")).hexdigest()

    with open(DIGEST_FILE, "r", encoding="utf-8") as digest_file:
        stored_digest = digest_file.read().strip()

    if hmac.compare_digest(entered_digest, stored_digest):
        print("Password verification successful.")
    else:
        print("Password verification failed.")