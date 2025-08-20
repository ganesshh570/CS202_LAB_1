def greet(name):
    print(f"Hello, {name}!")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(limit):
    sequence = [0, 1]
    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def squares(n):
    return [i ** 2 for i in range(1, n + 1)]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_up_to(n):
    return [x for x in range(2, n+1) if is_prime(x)]

if __name__ == "__main__":
    greet("Ganesh")
    print("Factorial of 5:", factorial(5))
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("Squares up to 5:", squares(5))
    print("Primes up to 20:", primes_up_to(20))
  
