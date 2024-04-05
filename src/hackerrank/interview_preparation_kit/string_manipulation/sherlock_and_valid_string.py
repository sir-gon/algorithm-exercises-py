def char_to_dict(a: str) -> dict:
    a_map = {char: (a.count(char)) for char in ''.join(sorted(a[:]))}

    return a_map


def is_valid(s: str) -> bool:

    if len(s) <= 1:
        return True

    string_map = char_to_dict(s)
    sorted_string_map = dict(sorted(string_map.items(), key=lambda x: x[1]))

    tolerance_range = 1
    tolerance_times = 1

    last = 0

    for _, x in sorted_string_map.items():
        if last == 0:
            last = x
            continue

        if x != last:
            if tolerance_times > 0:
                tolerance_times -= 1
            else:
                return False

            diff = x - tolerance_range
            if diff == 0:
                continue

            if diff != last:
                return False

    return True
