import unittest
from src.contacts import ContactsBook

class test_contacts_book(unittest.TestCase):
    def test_add_contact(self):
        book = ContactsBook()
        # name and phone number are fake and not real
        book.add_contact("John", "09004582971")
        self.assertEqual(len(book,contacts), 1)
        