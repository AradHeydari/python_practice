import unittest
from src.contacts import ContactsBook

class test_contacts_book(unittest.TestCase):
    def test_add_contact(self):
        book = ContactsBook()
        # name and phone number are fake and not real
        book.add_contact("John", "09004582971")
        self.assertEqual(len(book.contacts), 1)
        
    def test_list_contacts(self):
        book = ContactsBook()
        # name and phone number are fake and not real
        book.add_contact("Sara", "09010982457")
        self.assertEqual(book.list_contacts(), [{"name": "Sara","phone": "09010982457"}])