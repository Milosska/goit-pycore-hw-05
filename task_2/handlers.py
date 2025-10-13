from decimal import Decimal, ROUND_HALF_EVEN
from typing import Generator
from generator import generator_numbers

# Function to calculate the total sum of numbers extracted from text.
# Accepts a text string and a generator function that yields strings representing numbers.
# Converts each yielded number to Decimal for precise arithmetic.
# @returns the total sum as a float rounded to 2 decimal places using "round half even" method.
def sum_profit(text: str, generator: Generator[str, None, None]) -> float:
    try:
        text_generator = generator(text)
        total_sum = sum(Decimal(num) for num in text_generator)
        total_sum_rounded = float(total_sum.quantize(Decimal('0.00'), rounding=ROUND_HALF_EVEN))
    
        print(f"Загальний дохід: {total_sum_rounded}")
        return total_sum_rounded
    
    except AttributeError:
        print ("Provided text has no valid numbers to sum up.")

# Test cases
if __name__ == "__main__":
    text1 = "Base salary 1000.01 plus bonus 27.45 and 324.00 dollars."
    assert sum_profit(text1, generator_numbers) == 1351.46
    
    text2 = "No income here."
    assert sum_profit(text2, generator_numbers) is None
    
    text3 = "Small payments: 5 10 15"
    assert sum_profit(text3, generator_numbers) == 15.00 # Last 15 is ignored due to lack of surrounding spaces