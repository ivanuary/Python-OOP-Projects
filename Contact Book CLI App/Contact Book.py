#Class
class Contact():
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number

    def change_name(self, new_name):
        self.name = new_name
    
    def change_email(self, new_email):
        self.email = new_email

    def change_number(self, new_number):
        self.number = self.number

#Functions
def view_contacts(arr:list):
    for i, item in enumerate(arr, start=0):
        print(f"NAME: {arr[i].name} || EMAIL: {arr[i].email} || NUMBER: {arr[i].number}")

#Start
contacts = []
while True:
    print("""============
CONTACT BOOK
============
1. Add Contact
2. View Contacts
3. Edit Contacts
4. Exit
============""")
    menu_choice = input("ENTER CHOICE: ")
    if menu_choice == '1':
        print("============")
        name = input("ENTER NAME: ")
        email = input("ENTER EMAIL ADDRESS: ")
        number = input("ENTER PHONE NUMBER: ")
        contacts.append(Contact(name, email, number))
    elif menu_choice == '2':
        print("============")
        view_contacts(contacts)
    elif menu_choice == '3':
        print("============")
    elif menu_choice == '4':
        print("============")
    else:
        print("============")