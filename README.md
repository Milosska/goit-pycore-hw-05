## Task 1

### Task description

Implement a function caching_fibonacci that creates and uses a cache to store and reuse previously calculated Fibonacci numbers.

Requirements:

1. The function caching_fibonacci() must return an inner function fibonacci(n).
2. The inner function fibonacci(n) should compute the n-th Fibonacci number.
3. If the number is already in the cache, the function should return the cached value.
4. If the number is not in the cache, the function should compute it, store it in the cache, and then return the result.
5. Use recursion to calculate Fibonacci numbers.

### Execution

1. Open your terminal or command prompt.
2. Navigate to the task_1 folder:

```
cd task_1
```

3. Run the script using Python:

```
python main.py
```

4. The program will execute and display the results directly in the terminal.

## Task 2

### Task description

You need to create a function generator_numbers that analyzes a text, identifies all valid numbers considered as parts of income, and returns them as a generator. The valid numbers in the text are correctly written and clearly separated by spaces on both sides. You also need to implement a function sum_profit that uses generator_numbers to sum these numbers and calculate the total profit.

Requirements:

1. The function generator_numbers(text: str) should accept a string as an argument and return a generator that iterates over all valid numbers in the text. Valid numbers are considered correctly written and clearly separated by spaces on both sides.
2. The function sum_profit(text: str, func: Callable) should use the generator_numbers generator to calculate the total sum of numbers in the input string and accept the generator function as an argument.
3. Use regular expressions to identify valid numbers in the text, taking into account that the numbers are clearly separated by spaces.
4. Use the yield statement in generator_numbers to create a generator.
5. Code quality, presence of comments, and adherence to PEP8 coding style.

### Execution

1. **Run the main program**

   Go to the `task_2` folder and run:

   ```bash
   python main.py
   ```

2. **Run the test cases**
   To test individual components:
   Run handlers.py directly to test sum_profit:

```
python handlers.py
```

Run generator.py directly to test generator_numbers:

```
python generator.py
```

> **Note:** Test code in each file is protected with `if __name__ == "__main__":`,
> so it only runs when executing the file directly, not when imported.

### Example Usage

```python
from handlers import sum_profit
from generator import generator_numbers

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
```

Expected output:

```yaml
Загальний дохід: 1351.46
```
