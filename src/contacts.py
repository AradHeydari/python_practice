class ContactsBook:
    def __init__(self):
        self.contacts : list[dict[str, str]] = []

    def add_contact(self, name: str, phone: str) -> None:
        self.contacts.append({"name": name, "phone": phone})