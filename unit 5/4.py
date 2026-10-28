CONFIDENTIAL_FILE = "confidential.txt"
DEMO_PASSWORD = "demo123"
MAX_ATTEMPTS = 3


def create_sample_file():
    """Create the sample file if it does not already exist."""
    try:
        with open(CONFIDENTIAL_FILE, "x", encoding="utf-8") as file:
            file.write(
                "This is sample confidential content.\n"
                "Only authenticated users should see this text.\n"
            )
        print(f"Created {CONFIDENTIAL_FILE}.")
    except FileExistsError:
        print(f"Using existing {CONFIDENTIAL_FILE}.")


def access_confidential_file():
    """Ask for the password and allow up to three attempts."""
    for attempt in range(MAX_ATTEMPTS):
        try:
            password = input("Enter the password to access the file: ")
        except EOFError:
            print("Invalid input: no password was provided.")
            return

        if password == DEMO_PASSWORD:
            try:
                with open(CONFIDENTIAL_FILE, "r", encoding="utf-8") as file:
                    print("\nAccess granted. Confidential contents:")
                    print(file.read(), end="")
            except FileNotFoundError:
                print(f"File not found: {CONFIDENTIAL_FILE}")
            return
        elif not password:
            print("Invalid input: password cannot be empty.")
        else:
            print("Incorrect password.")

        if attempt < MAX_ATTEMPTS - 1:
            print(f"{MAX_ATTEMPTS - attempt - 1} attempt(s) remaining.")

    print("Access denied: maximum failed attempts reached.")


if __name__ == "__main__":
    print("Demo only: the password is stored in plain text and is not suitable for real applications.")
    create_sample_file()
    access_confidential_file()