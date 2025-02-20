
def isPalindrome(num):
    digits = str(num)
    reversed_num = "".join(reversed(digits))

    return digits == reversed_num
