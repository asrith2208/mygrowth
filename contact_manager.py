contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"{name} added successfully!")

def view_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found!")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully!")
    else:
        print(f"{name} not found!")

def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"{name} updated successfully!")
    else:
        print(f"{name} not found!")

# User input loop
while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact number: ")
        add_contact(name, phone)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter contact name to update: ")
        phone = input("Enter new name: ")
        update_contact(name, phone)
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == "5":
        break
    else:
        print("Invalid choice! Try again.")
