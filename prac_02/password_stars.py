
MINIMUM_LENGTH = 4


def main():
    """Get password and print the input using functions."""
    password = get_password(MINIMUM_LENGTH)
    display_asterisks(password)


def get_password(minimum_length):
    """Get suitable password, exceeding minimum length."""
    password = input(f"Enter password (At least 4 characters): ")
    while len(password) < minimum_length:
        print("Password has to contain at least 4 characters")
        password = input(f"Enter password (At least 4 characters): ")
    return password


def display_asterisks(characters):
    """Print asterisks according to password characters."""
    print('*' * len(characters))


main()
