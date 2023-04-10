"""
Emails
Estimate: 25 minutes
Actual: minutes
"""


def main():
    """Main function to stores and displays users' input when enter a blank"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        check = input(f"Is your name {name}? (Y/n) ").upper()
        if check != "Y" and check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """This function is to extract a name from email input"""
    name_from_email = email.split('@')[0]
    name_parts = name_from_email.split('.')
    name = " ".join(name_parts).title()
    return name


main()
