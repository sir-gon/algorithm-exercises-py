from collections import Counter


def char_to_dict(a: str) -> dict:
    a_map = {char: (a.count(char)) for char in ''.join(sorted(a[:]))}

    return a_map


def is_valid(s: str) -> bool:

    if len(s) <= 1:
        return True

    string_map = char_to_dict(s)
    frequencies = Counter(string_map.values())
    frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1]))
    frequencies_size = len(frequencies)

    if frequencies_size == 1:
        return True

    if frequencies_size > 2:
        return False

    if frequencies_size == 2:
        frequencies_list = list(frequencies.keys())

        if frequencies[frequencies_list[0]] == 1 and \
            (frequencies_list[0] - 1 == 0 or
             frequencies_list[0] - 1 == frequencies_list[1]):
            return True

    return False
