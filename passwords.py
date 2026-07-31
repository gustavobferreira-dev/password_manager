import string
import secrets


def add_password(profile_list, website, username, password):
    """
    Add a new password profile.

    Prevent duplicate websites and empty fields.
    """

    website = website.strip()
    username = username.strip()
    password = password.strip()

    if not website:
        print("\nWebsite cannot be empty.")
        return

    if not username:
        print("\nUsername cannot be empty.")
        return

    if not password:
        print("\nPassword cannot be empty.")
        return

    # Check if the website already exists.
    for profile in profile_list:
        if profile["website"].lower() == website.lower():
            print("\nThis website is already registered.")
            return

    profile_list.append({
        "website": website,
        "username": username,
        "password": password,
    })

    print("\nPassword added successfully!")


def show_passwords(profile_list):
    """
    Display every saved profile.
    """

    if not profile_list:
        print("\nNo passwords found.")
        return

    print("\n" + "=" * 60)
    print("                 SAVED PASSWORDS")
    print("=" * 60)

    for index, profile in enumerate(profile_list, start=1):

        hidden_password = "*" * len(profile["password"])

        print(f"""
ID       : {index}
Website  : {profile["website"]}
Username : {profile["username"]}
Password : {hidden_password}
{"-" * 60}""")


def edit_password(profile_list, profile_id):
    """
    Update a password using its ID.
    """

    if profile_id < 1 or profile_id > len(profile_list):
        print("\nInvalid ID.")
        return

    profile = profile_list[profile_id - 1]

    print(f"\nSelected website: {profile['website']}")

    new_password = input("New password\n--> ").strip()

    if not new_password:
        print("\nPassword cannot be empty.")
        return

    profile["password"] = new_password

    print("\nPassword updated successfully!")


def delete_password(profile_list, profile_id):
    """
    Delete a profile using its ID.
    """

    if profile_id < 1 or profile_id > len(profile_list):
        print("\nInvalid ID.")
        return

    removed_profile = profile_list.pop(profile_id - 1)

    print(
        f"\n'{removed_profile['website']}' deleted successfully!"
    )


def search_password(profile_list, website):
    """
    Search for a saved profile.
    """

    for profile in profile_list:

        if profile["website"].lower() == website.lower():

            hidden_password = "*" * len(profile["password"])

            print("\nProfile found!")
            print("-" * 40)
            print(f"Website  : {profile['website']}")
            print(f"Username : {profile['username']}")
            print(f"Password : {hidden_password}")
            print("-" * 40)

            choice = input("\nReveal password? (Y/N)\n--> ").strip().upper()

            if choice == "Y":
                print(f"\nPassword: {profile['password']}")

            return

    print("\nThis website is not registered.")


def generate_password(profile_list, length):
    """
    Generate a secure random password.
    """

    if length < 8:
        print("\nPassword must contain at least 8 characters.")
        return

    alphabet = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )

    hidden_password = "*" * len(password)

    print("\nGenerated password:")
    print(hidden_password)

    choice = input("\nReveal password? (Y/N)\n--> ").strip().upper()

    if choice == "Y":
        print(f"\n{password}")

    choice = input("\nUse this password? (Y/N)\n--> ").strip().upper()

    if choice != "Y":
        print("\nPassword discarded.")
        return

    website = input("\nWebsite\n--> ").strip()

    username = input("Username\n--> ").strip()

    add_password(
        profile_list,
        website,
        username,
        password
    )