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