# Week 6 - Day 2 - Practice 2
# Fibonacci Sequence Generator

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
