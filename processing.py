from error_processing import input_error
from models import AddressBook, Record

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, contacts: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = contacts.find(name)
    message = "Contact updated."
    if record is None:
        message = "Contact not found."
    else:
        record.edit_phone(old_phone, new_phone)
    return message    

@input_error
def contact_phone(args, contacts: AddressBook):
    name, *_ = args
    return "\n".join(contacts.find(name).phones)

@input_error
def all_contacts(args, contacts: AddressBook):
    return "\n".join(list(contacts.values()))

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added"

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    return record.birthday

@input_error
def birthdays(args, book: AddressBook):
    return "\n".join(list([r.birthday for r in book.get_upcoming_birthdays()]))
