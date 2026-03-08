from error_processing import input_error
from models import AddressBook

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

@input_error
def contact_phone(args, contacts: dict):
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def all_contacts(args, contacts: dict):
    return "\n".join(list(contacts.values()))

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    contact = book.find(name)
    contact.add_birthday(birthday)
    return "Birthday added"

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    return contact.birthday

@input_error
def birthdays(args, book: AddressBook):
    return "\n".join(list([r.birthday for r in book.get_upcoming_birthdays()]))
