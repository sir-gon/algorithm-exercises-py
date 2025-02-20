def isPrime(num):
    if num in (0, 1):
        return False

    for i in range(2, num):
        if 0 == num % i:
            return False

    return True
