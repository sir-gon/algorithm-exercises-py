# @link Problem definition [[docs/hackerrank/projecteuler/euler002.md]]
# pylint: disable=C0103:invalid-name

def fiboEvenSum(n: int) -> int:
    total = 0
    fibo = 0
    fibo1 = 1
    fibo2 = 1

    while fibo1 + fibo2 < n:
        fibo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo

        if fibo % 2 == 0:
            total += fibo

    return total


def euler002(n: int) -> int:

    return fiboEvenSum(n)
