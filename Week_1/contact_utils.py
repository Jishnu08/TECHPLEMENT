import os
import re

FILENAME = "contacts.txt"

# -------------------- File I/O --------------------

def load_contacts():
    contacts = []
    if not os.path.exists(FILENAME):
        return contacts

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    contacts.append({
                        "name": parts[0],
                        "phone": parts[1],
                        "email": parts[2]
                    })
    except Exception as e:
        print(f"Error reading file: {e}")
    return contacts

def save_contacts(contacts):
    try:
        with open(FILENAME, "w") as file:
            for contact in contacts:
                line = f"{contact['name']}|{contact['phone']}|{contact['email']}\n"
                file.write(line)
    except Exception as e:
        print(f"Error writing to file: {e}")

# -------------------- Validate --------------------

def is_valid_name(name):
    return bool(name.strip()) and all(part.isalpha() for part in name.split())

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# -------------------- Main Work --------------------

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not is_valid_name(name):
        print("❌ Invalid name. Only letters and spaces allowed.")
        return
    if not is_valid_phone(phone):
        print("❌ Invalid phone number. Must be 10 digits.")
        return
    if not is_valid_email(email):
        print("❌ Invalid email format.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("❌ Contact already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("✅ Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if name in contact['name'].lower():
            print(f"✅ Found: {contact['name']} - {contact['phone']} - {contact['email']}")
            found = True
    if not found:
        print("No contact found with that name.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            new_phone = input(f"Enter new phone (current: {contact['phone']}): ").strip()
            new_email = input(f"Enter new email (current: {contact['email']}): ").strip()

            if new_phone and not is_valid_phone(new_phone):
                print("❌ Invalid phone number. Skipping update.")
            else:
                contact['phone'] = new_phone or contact['phone']

            if new_email and not is_valid_email(new_email):
                print("❌ Invalid email. Skipping update.")
            else:
                contact['email'] = new_email or contact['email']

            print("✅ Contact updated.")
            return
    print("Contact not found.")
