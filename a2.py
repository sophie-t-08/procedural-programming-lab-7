n = int(input("Enter a number: "))
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return a

print(fibonacci_iterative(n))

n = n = int(input("Enter a number: "))
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(n))