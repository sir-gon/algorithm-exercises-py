def product(_list_of_numbers: list):
    size = len(_list_of_numbers)
    if size == 0:
        return 0

    acum = 1
    for i in range(0, size):
        acum *= int(_list_of_numbers[i])

    return acum
