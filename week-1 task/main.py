import csv

# File to store contacts
filename = 'contacts.csv'


def create_file():
    try:
        with open(filename, mode='x') as f:
            writer = csv.writer(f)
            writer.writerow(["First Name", "Last Name", "Phone Number", "Email", "Work Location"])
    except FileExistsError:
        pass


def add_contact(first_name, last_name, phone_number, email, work_location):
    if first_name and last_name and phone_number and email and work_location:
        with open(filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([first_name, last_name, phone_number, email, work_location])
    else:
        print("Error: All fields must be filled.")


def search_contact(search_term):
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        found = False
        for row in reader:
            if search_term.lower() in [item.lower() for item in row]:
                print(f"Found Contact: {row}")
                found = True
        if not found:
            print("No matching contacts found.")


def update_contact(search_term, new_first_name, new_last_name, new_phone_number, new_email, new_work_location):
    updated = False
    with open(filename, mode='r') as f:
        rows = list(csv.reader(f))

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            if search_term.lower() in [item.lower() for item in row]:
                row = [
                    new_first_name if new_first_name else row[0],
                    new_last_name if new_last_name else row[1],
                    new_phone_number if new_phone_number else row[2],
                    new_email if new_email else row[3],
                    new_work_location if new_work_location else row[4]
                ]
                updated = True
            writer.writerow(row)

    if updated:
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact(search_term):
    deleted = False
    with open(filename, mode='r') as f:
        rows = list(csv.reader(f))

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            if search_term.lower() not in [item.lower() for item in row]:
                writer.writerow(row)
            else:
                deleted = True

    if deleted:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def display_contacts():
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def main():
    create_file()
    while True:
        print(
            "\n1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. Display All Contacts\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            work_location = input("Enter Work Location (Home/Office): ")
            add_contact(first_name, last_name, phone_number, email, work_location)
        elif choice == '2':
            search_term = input("Enter Name, Phone Number, or Email to Search: ")
            search_contact(search_term)
        elif choice == '3':
            search_term = input("Enter Name, Phone Number, or Email to Update: ")
            new_first_name = input("Enter New First Name (Leave blank to skip): ")
            new_last_name = input("Enter New Last Name (Leave blank to skip): ")
            new_phone_number = input("Enter New Phone Number (Leave blank to skip): ")
            new_email = input("Enter New Email (Leave blank to skip): ")
            new_work_location = input("Enter New Work Location (Leave blank to skip): ")
            update_contact(search_term, new_first_name, new_last_name, new_phone_number, new_email, new_work_location)
        elif choice == '4':
            search_term = input("Enter Name, Phone Number, or Email to Delete: ")
            delete_contact(search_term)
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
