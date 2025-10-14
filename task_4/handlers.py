from helpers import normalize_phone, check_if_in_contacts
from decorators import input_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if check_if_in_contacts(name.capitalize(), contacts):
        raise ValueError("Contact already exists.")
    
    contacts[name.capitalize()] = normalize_phone(phone)
    return "Contact added."
    
@input_error
def update_contact(args, contacts):
    name, phone = args

    if not check_if_in_contacts(name.capitalize(), contacts):
        raise ValueError("Contact not found.")
    
    contacts[name.capitalize()] = normalize_phone(phone)
    return "Contact updated."

@input_error
def show_contact_number(args, contacts):
    name = args[0]
    return contacts[name.capitalize()]

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts added."
    else:
        constact_list = 'Your contacts:'
        for name, phone in contacts.items():
            constact_list += f"\n{' '*2}{name}: {phone}"

        return constact_list
