addressbook = {}
def ak(name, phone_number, email):
    addressbook[name] = {'phone_number': phone_number, 'email': email}
    print(f" {name} details added successfully.")
def contact():
    if not addressbook:
        print("Address book is empty.")
    else:
        for name, details in addressbook.items():
            print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}")
def delete_details(name):
    if name in addressbook:
        del addressbook[name]
        print(f"{name} contact details deleted successfully.")
    else:
        print(f"Contact {name} not found in the address book.")
ak("david", "1234565412", "davidd@gmail.com")
ak("kholi", "9878998765", "kholi12@gmail.com")
contact()
delete_details("david")
contact()