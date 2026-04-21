import secrets
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters")

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # ensure at least one of each type
    password = [
        secrets.choice(uppercase_letters),
        secrets.choice(lowercase_letters),
        secrets.choice(digits),
        secrets.choice(special_characters),
    ]

    # fill remaining length
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # shuffle for randomness
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    try:
        password_length = int(input("Enter password length (min 6): "))
        print("Generated Password:", generate_password(password_length))
    except ValueError as e:
        print(e)