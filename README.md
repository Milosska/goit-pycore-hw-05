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

## Task 3

### Task description

Develop a Python script for analyzing log files. The script should be able to read a log file provided as a command-line argument and display statistics by log levels, for example, INFO, ERROR, DEBUG. Additionally, the user can specify a log level as a second command-line argument to see all entries of that level.

Requirements:

1. The script fulfills all the requirements, correctly analyzing log files and displaying the information.
2. The script properly handles errors, such as incorrect log file format or missing file.
3. During development, at least one element of functional programming must be used: a lambda function, list comprehension, the filter function, etc.
4. The code is well-structured, clear, and contains comments where necessary.

### Execution

1. **Run the main program**

To see the logs statistics go to the `task_3` folder and run:

```bash
python main.py [path/to/log/file]
```

To see the logs per type run:

```bash
python main.py [path/to/log/file] [log_type]
```

2. **Run the test cases**
   To test individual components run test files as modules:

```bash
python -m tests.handlers_tests
```

### Example Usage

```bash
python main.py logs.txt error
```

Expected output:

```yaml
-----------------|----------
DEBUG            | 3
INFO             | 4
WARNING          | 1
ERROR            | 2

Деталі логів для рівня ERROR:
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

## Task 4

### Task description

Complete the console assistant bot from the previous homework and add error handling using decorators.

Requirements:

1. All user input errors must be handled using the input_error decorator.
2. This decorator is responsible for returning user-friendly messages such as "Enter user name", "Give me name and phone please", etc.
3. The input_error decorator must handle exceptions that occur in the handler functions — specifically: KeyError, ValueError, and IndexError.
4. When an exception occurs, the decorator should return an appropriate response message to the user, without terminating the program’s execution.

### Execution

1. Open a terminal and navigate to the `task_4` folder:

   ```bash
   cd path/to/task_4
   ```

2. Run the console bot script:

   ```bash
   python main.py
   ```

3. The program will wait for your commands. Use valid commands listed in the commnds section.

### Comands

The assistant supports the following commands:

- **`hello`** — greets the user with a friendly message.
- **`add [name] [phone number]`** — adds a new contact to the contact list.
- **`change [name] [new phone number]`** — updates the phone number of an existing contact.
- **`phone [name]`** — displays the phone number of the specified contact.
- **`all`** — shows all saved contacts with their phone numbers.
- **`close`** or **`exit`** — ends the program with a farewell message.

Any command that does not match the formats above will be considered invalid.
Commands are case-insensitive.
