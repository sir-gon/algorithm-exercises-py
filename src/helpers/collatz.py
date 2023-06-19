# Collatz sequence
#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)
# example:
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

def collatz(_n: int) -> int:
    if _n % 2 == 0:
        return int(_n / 2)

    return 3 * _n + 1
