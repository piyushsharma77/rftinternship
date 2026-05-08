phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780"
}


def add_contact():
    name = input("Enter name: ").upper()
    number = input("Enter number: ")

    if name in phonebook:
        print("Contact already exists!")
    else:
        phonebook[name] = number
        print("Contact added successfully.")


def search_contact():
    search = input("Enter name to search: ").upper()
    found = False

    for name in phonebook:
        if search in name:
            print(name, ":", phonebook[name])
            found = True

    if not found:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").upper()

    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def show_all():
    if phonebook:
        print("\nPhonebook:")
        for name, number in phonebook.items():
            print(name, ":", number)
    else:
        print("Phonebook is empty.")


while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        show_all()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")