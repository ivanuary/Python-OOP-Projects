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
        self.number = new_number

#Functions
def view_contacts(arr:list):
    for i, item in enumerate(arr, start=0):
        print(f"ENTRY #{i+1} || NAME: {arr[i].name} || EMAIL: {arr[i].email} || NUMBER: {arr[i].number}")

def check_int():
    while True:
        try:
            num_int = int(input("ENTER NUMBER: "))
            return num_int
        except ValueError:
            print("Not a valid number! Please Try Again")

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
        view_contacts(contacts)
        print("============")
        print("""SELECT ENTRY TO EDIT...""")
        while True:
            entry_edit = check_int()
            if entry_edit > len(contacts) or entry_edit < 1:
                print("INVALID INPUT, TRY AGAIN\n")
            else:
                contacts[entry_edit-1].change_name(input("Enter New Name: "))
                contacts[entry_edit-1].change_email(input("Enter New Email: "))
                contacts[entry_edit-1].change_number(input("Enter New Number: "))
                break
    elif menu_choice == '4':
        print("============")
        quit()
    else:
        print("============")
        print("INVALID INPUT, PLEASE TRY AGAIN")