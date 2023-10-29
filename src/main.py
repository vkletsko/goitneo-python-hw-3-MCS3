from models.address_book import AddressBook
from models.record import Record
from validators.validate_input import input_error
from utils.parse_input import parse_input


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args

    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added"


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, old_phone, new_phone = args
    search_record = contacts.find(name)
    search_record.edit_phone(old_phone, new_phone)
    return "Contact updated"


@input_error
def show_phone(args: list, contacts: dict) -> str:
    search_name = args[0]

    contacts.find(search_name)

    for name, phone in contacts.items():
        if search_name == name:
            return f"{search_name.title()} {phone}"
        else:
            return f"Contact {search_name.title()} doesn't exist"


@input_error
def show_all(contacts: dict) -> str:
    phonebook = "Contacts list: \n"

    for name, info in contacts.items():
        phones = ""
        for phone in info.phones:
            phones += str(phone)
        phonebook += "Contact: {} {}\n".format(name.title(), phone)

    return phonebook


@input_error
def set_birthday(args: list, contacts: dict) -> None:
    name, b_date = args
    contacts.set_birthday(name, b_date)
    print("Birthday added")


def show_birthday(args: list, contacts: dict) -> None:
    name = str(args[0])
    contact_bday = contacts.show_birthday(name)
    print(contact_bday)


def happy_birthdays(contacts: dict) -> None:
    birthdays = contacts.get_birthdays_per_week()
    print(birthdays)


def main():
    address_book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        cmd, *args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, address_book))
        elif cmd == "change":
            print(change_contact(args, address_book))
        elif cmd == "phone":
            print(show_phone(args, address_book))
        elif cmd == "all":
            print(show_all(address_book))
        elif cmd == "add-birthday":
            set_birthday(args, address_book)
        elif cmd == "show-birthday":
            show_birthday(args, address_book)
        elif cmd == "birthdays":
            happy_birthdays(address_book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
