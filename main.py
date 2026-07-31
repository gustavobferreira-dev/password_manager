from passwords import (
    add_password,
    show_passwords,
    search_password,
    edit_password,
    generate_password,
    delete_password,
)
from storage import load_profiles, save_profiles


def display_menu():
    print("\n" + "=" * 40)
    print("          PASSWORD MANAGER")
    print("=" * 40)
    print("1 - Add Password")
    print("2 - Show Passwords")
    print("3 - Search Password")
    print("4 - Edit Password")
    print("5 - Remove Password")
    print("6 - Generate Password")
    print("7 - Save Passwords")
    print("0 - Exit")


def main():
    profile_list = load_profiles()

    while True:
        display_menu()

        try:
            user_choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nPlease enter numbers only.")
            continue

        match user_choice:
            case 1:
                add_password(
                    profile_list,
                    input("\nWrite your Website's name.\n--> ").strip(),
                    input("Write your Username\n--> ").strip(),
                    input("Write your Password\n--> ").strip(),
                )
            case 2:
                show_passwords(profile_list)
            case 3:
                search_password(profile_list, input("\nWrite your profile's website.\n--> ").strip().lower())
            case 4:
                show_passwords(profile_list)

                try:
                    profile_id = int(input("\nSelect the ID to edit\n--> "))
                except ValueError:
                    print("\nInvalid ID.")
                    continue

                edit_password(profile_list, profile_id)
            case 5:
                show_passwords(profile_list)

                try:
                    profile_id = int(input("\nSelect the ID to delete\n--> "))
                except ValueError:
                    print("\nInvalid ID.")
                    continue

                delete_password(profile_list, profile_id)
            case 6:
                try:
                    password_length = int(input("\nPlease, enter with the length of your desired password.\n--> "))
                except ValueError:
                    print("\nPlease enter a valid number.")
                    continue

                generate_password(profile_list, password_length)
            case 7:
                save_profiles(profile_list)
                print("\nPasswords saved successfully!")
            case 0:
                save_profiles(profile_list)
                print("\nGoodbye!")
                break
            case _:
                print("\nInvalid option.")


if __name__ == "__main__":
    main()
