import re
from typing import Generator

# Generator function to extract numbers from a given text.
# Matches both integers and decimal numbers.
# The numbers are expected to be surrounded by whitespace.
# @yields strings representing the numbers found, with surrounding whitespace removed.
def generator_numbers(text: str) -> Generator[str, None, None]:
    start_index = 0
    pattern = r"\s(\d+(?:\.\d+)?)\s"
    
    while start_index < len(text):
        match = re.search(pattern, text[start_index:])
        if not match:
            break  

        # Move 1 step back for cases when numbers go one after another with only one space in between
        start_index += (match.end() - 1)
        yield match.group().strip()

# Test cases
if __name__ == "__main__":
    numbers1 = list(generator_numbers("No numbers here!"))
    assert numbers1 == []
    
    numbers2 = list(generator_numbers("The price is 100.50 dollars and the tax is 5.75 dollars."))
    assert numbers2 == ["100.50", "5.75"]
    
    numbers3 = list(generator_numbers("Leading 42 and trailing 99.99 "))
    assert numbers3 == ["42", "99.99"]
    
    numbers4 = list(generator_numbers("Mixed 123text456 and 78.90 numbers."))
    assert numbers4 == ["78.90"]
    
    numbers5 = list(generator_numbers("Multiple 1.1 2.1 numbers 2.2line"))
    assert numbers5 == ["1.1", "2.1"]