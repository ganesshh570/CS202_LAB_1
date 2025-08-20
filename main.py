"""
Sample Python project for GitHub Actions + pylint lab.
"""

def greet(name: str) -> None:
    """Print a greeting."""
    print(f"Hello, {name}!")


def factorial(n: int) -> int:
    """Return factorial of n."""
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(limit: int) -> list[int]:
    """Return a Fibonacci sequence up to limit numbers."""
    sequence = [0, 1]
    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def squares(n: int) -> list[int]:
    """Return a list of squares up to n."""
    return [i ** 2 for i in range(1, n + 1)]


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_up_to(n: int) -> list[int]:
    """Return all prime numbers up to n."""
    return [x for x in range(2, n + 1) if is_prime(x)]


if __name__ == "__main__":
    greet("Ganesh")
    print("Factorial of 5:", factorial(5))
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("Squares up to 5:", squares(5))
    print("Primes up to 20:", primes_up_to(20))
