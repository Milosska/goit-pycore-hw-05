from typing import Callable

# Returns a Fibonacci function that uses memoization to cache results.
def caching_fibonacci() -> Callable[[int], int]:
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        
        elif n == 1:
            return 1
        
        elif n in cache:
            return cache[n]
        
        else: 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

fib = caching_fibonacci()

# Test cases
assert fib(0) == 0
assert fib(1) == 1
assert fib(10) == 55
assert fib(25) == 75025
assert fib(10) == 55