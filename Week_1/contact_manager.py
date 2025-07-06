from contact_utils import (
    load_contacts,
    save_contacts,
    add_contact,
    view_contacts,
    search_contact,
    update_contact
)

def main():
    contacts = load_contacts()

    while True:
        print("\n======= Contact Management System =======")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Update Contact Information")
        print("5. Exit")
        print("=========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
