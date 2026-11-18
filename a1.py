n = int(input("Enter a number: "))
def factorial_iterative(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial
print(factorial_iterative(n))

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_iterative(n-1)
print(factorial_recursive(n))