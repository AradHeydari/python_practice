import unittest
import os
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

    def test_search_contact(self):
        book = ContactsBook()
        # name and phone number are fake and not real
        book.add_contact("Tyler", "05679901503")
        result = book.search("Tyler")
        self.assertEqual(result[0]["phone"], "05679901503")

    def test_search_by_phone(self):
        book = ContactsBook()
        book.add_contact("Tyler", "05679901503")
        result = book.search("05679901503")
        self.assertEqual(result[0]["name"], "Tyler")

    def test_delete_contact(self):
        book = ContactsBook()
        # name and phone number are fake and not real
        book.add_contact("Melinda", "01925698875")
        book.delete("Melinda")
        self.assertEqual(len(book.contacts), 0)

    def test_delete_contact_by_phonenumber(self):
        book = ContactsBook()
        # name and phone number are fake and not real
        book.add_contact("Melinda", "01925698875")
        book.delete("01925698875")
        self.assertEqual(len(book.contacts), 0)

    def test_save_and_load(self):
        book = ContactsBook()
        book.add_contact("Test", "123")
        book.save_to_file("test.json")

        new_book = ContactsBook()
        new_book.load_from_file("test.json")
        self.assertEqual(new_book.list_contacts(), [{"name": "Test", "phone": "123"}])

        os.remove("test.json")

    