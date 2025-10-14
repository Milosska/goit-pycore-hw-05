import re

def check_if_in_contacts(name: str, contacts: dict) -> bool:
    return name in contacts

def normalize_phone(phone_number: str) -> str:
    # Remove all non-numeric characters except the leading '+'
    pattern = r"\+|\d+"
    matches = re.findall(pattern, phone_number)
    cleaned_number = ''.join(matches)

    if len(cleaned_number) < 7  or len(cleaned_number) > 13:
        raise ValueError("Invalid phone number length.")

    # Check the number begining and add missing parts
    if not cleaned_number.startswith('+'):
        cleaned_number = '+' + cleaned_number

    if cleaned_number.find('3') != 1:
        cleaned_number = cleaned_number.replace('+', '+3', 1)

    if cleaned_number.find('8') != 2:
        cleaned_number = cleaned_number.replace('+3', '+38', 1)

    return cleaned_number