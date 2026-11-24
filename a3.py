n = int(input("Enter a number: "))

def is_prime(n):
    if n <= 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True
print(is_prime(n))