class Contact:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail: {self.email}'


contacts = []

print('\tPHONE BOOK')

print('OPTIONS:\n[1] - ADD CONTACT | [2] - UPDATE CONTACT | [3] - DELETE CONTACT | [4] LIST CONTACTS | [0] EXIT')
while True:
    option = int(input('YOUR OPTION: '))
    if option == 0:
        print("THANKS FOR USING PHONE BOOK!")
        break
    elif option == 1:
        info = input(
            'NAME, ADDRESS, PHONE, NUMBER, EMAIL(SEPARATED BY " ")\n>>> ')
        info = info.split()
        contacts.append(Contact(info[0], info[1], info[2], info[3]))
    elif option == 2:
        for contact in contacts:
            print(f"ALL CONTACTS' NAMES:\n   - {contact.name}")
        contact_to_update = input("WHICH CONTACT TO UPDATE? ")
        for contact in contacts:
            if contact.name == contact_to_update:
                info_to_update = input(
                    "WHAT TO UPDATE: NAME, ADDRESS, PHONE NUMBER, EMAIL? ").lower()
                new_info = input(f"UPDATE {info_to_update.upper()} TO: ")
                if info_to_update == 'name':
                    contact.name = new_info
                elif info_to_update == 'address':
                    contact.address = new_info
                elif info_to_update == 'phone number':
                    contact.phone_number = new_info
                elif info_to_update == 'email':
                    contact.email = new_info
                else:
                    print("NO SUCH INFORMATION FOR THE CONTACT")
            else:
                print("NO SUCH CONTACT")

    elif option == 3:
        for contact in contacts:
            print(f"ALL CONTACTS' NAMES:\n   - {contact.name}")
        contact_to_delete = input("WHICH CONTACT TO DELETE? ")
        for contact in contacts:
            if contact.name == contact_to_delete:
                contacts.remove(contact)
            else:
                print("NO SUCH CONTACT")
    elif option == 4:
        print("CONTACTS INFO:\n")
        for contact in contacts:
            print(contact)
            print()
    else:
        print("NO SUCH OPTION. TRY AGAIN.")
