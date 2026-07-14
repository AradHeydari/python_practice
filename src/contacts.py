import json
from typing import List, Dict
class ContactsBook:
    def __init__(self):
        self.contacts : list[dict[str, str]] = []

    def add_contact(self, name: str, phone: str) -> None:
        self.contacts.append({"name": name, "phone": phone})

    def list_contacts(self):
        return self.contacts
    
    def search(self, n_p): #n_p stands for name or phone 
        return [c for c in self.contacts if c["name"] == n_p or c["phone"] == n_p]
    
    def delete(self, identifier):
        self.contacts = [x for x in self.contacts if x["name"] != identifier and x["phone"] != identifier]

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.contacts, f)

    def load_file(self, filename):
        with open(filename, "r") as f:
            self.contacts = json.load(f)




def main():
    book = ContactsBook()
    try:
        book.load_file("contacts.json")
        print("information loaded")
    except FileNotFoundError:
        print("no file found. new book added")

    while True:
    
        print("\n contacts book")
        print("1. add contact")
        print("2. show all contacts")
        print("3. search contact")
        print("4. delete contact")
        print("5. save and exit")
        choice = input("chose from (1-5): ")

        if choice == "1":
            name = input("name: ")
            phone = input("phone number: ")
            book.add_contact(name, phone)
            print("contact added")

        elif choice == "2":
            contacts = book.list_contacts()
            if not contacts:
                print("book is empty")
            else:
                for i, c in enumerate(contacts, 1):
                    print(f"{i}. {c['name']} - {c['phone']}")

        elif choice == "3":
            xyz = input("enter name or phone number:")
            results = book.search(xyz)
            if results:
                for c in results:
                    print(f"--> {c['name']} - {c['phone']}")
            else:
                print("no contacts added")

        elif choice == "4":
            xyz = input("name or phone number: ")
            book.delete(xyz)
            print("contact has been deleted")

        elif choice == "5":
            book.save_to_file("contacts.json")
            print("information has been saved. \n Goodbye")
            break

        else:
            print("invalid choice. \n try again")

    
if __name__ == "__main__":
    main()

