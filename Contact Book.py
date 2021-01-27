contacts = {}


def get_info():
    name = input("Contact Name: ")
    address = input("Contact Address: ")
    phone_number = input("Contact Phone Number: ")
    email = input("Contact Email: ")
    return name, address, phone_number, email


def add_contact(name, address, phone_number, email):
    if name not in contacts.keys():

        contacts[name] = [address, phone_number, email]
    else:
        print("That contact exists.")


def update_contact(contact_to_update):
    if contact_to_update in contacts.keys():
        print('Contact Info:')
        print("Name:", contact_to_update)
        print("Address:", contacts[contact_to_update][0])
        print("Phone:", contacts[contact_to_update][1])
        print("Email:", contacts[contact_to_update][2])
        info_to_update = input(
            'Which information to update? (Name or Address or Phone or Email) ').lower()
        change = input("Change: ")
        if info_to_update == 'name':
            contacts[change] = contacts[contact_to_update]
            del contacts[contact_to_update]
        elif info_to_update == 'address':
            contacts[contact_to_update][0] = change
        elif info_to_update == 'phone':
            contacts[contact_to_update][1] = change
        elif info_to_update == 'email':
            contacts[contact_to_update][2] = change
        else:
            print('No such information for the contact.')
    else:
        print("No such contact in Contact book.")


def delete_contact(contact_to_delete):
    if contact_to_delete in contacts.keys():
        del contacts[contact_to_delete]
    else:
        print("No such contact in Contact Book.")


print('Contact Book')
print('Options: Add Contact, Update Contact, Delete Contact, List Contacts, Exit')


def main():
    while True:

        option = input("Your Option: ").lower()

        if option == 'exit':
            print("See ya soon!")
            break

        elif option == 'add contact':
            name, address, phone_number, email = get_info()
            add_contact(name, address, phone_number, email)

        elif option == 'update contact':
            contact_to_update = input('Which contact to update? ')
            update_contact(contact_to_update)

        elif option == 'delete contact':
            contact_to_delete = input('Which contact to delete? ')
            delete_contact(contact_to_delete)

        elif option == 'list contacts':
            if contacts:
                for contact, info in sorted(contacts.items()):
                    print(
                        f"Name: {contact}, Address: {info[0]}, Phone Number: {info[1]}, Email: {info[2]}")
                    print()
            else:
                print("Empty Contact Book")
        else:
            print("No such option")


main()
