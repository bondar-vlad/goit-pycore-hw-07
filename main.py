from data_parcers import parse_input
from cli_processing import add_contact, change_contact, contact_phone, all_contacts, add_birthday, show_birthday, birthdays

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(contact_phone(args, contacts))
            case "all":
                print(all_contacts(args, contacts))
            case "add-birthday":
                print(add_birthday(args, contacts))
            case "show-birthday":
                print(show_birthday(args, contacts))
            case "birthdays":
                print(birthdays(args, contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
