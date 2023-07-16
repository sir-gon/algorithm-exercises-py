# Import math library
import math

_CENTS_ = 'hundred'
_MILLS_ = 'thousand'

dictionary = {
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
  '10': 'ten',
  '11': 'eleven',
  '12': 'twelve',
  '13': 'thirteen',
  '14': 'fourteen',
  '15': 'fifteen',
  '16': 'sixteen',
  '17': 'seventeen',
  '18': 'eighteen',
  '19': 'nineteen',
  '20': 'twenty',
  '30': 'thirty',
  '40': 'forty',
  '50': 'fifty',
  '60': 'sixty',
  '70': 'seventy',
  '80': 'eighty',
  '90': 'ninety',
  '100': 'hundred',
  '1000': 'thousand'
}


def number_to_word(value: int) -> str:
    big_value = str(value)

    # 1 to 19
    if len(big_value) <= 2 and 0 < value <= 19:
        return dictionary[big_value]

    # 20 to 99
    if len(big_value) == 2 and 20 <= value <= 99:
        dec = math.floor(value / 10) * 10
        unit = math.floor(value % 10)

        if unit == 0:
            return dictionary[str(dec)]

        return f"{dictionary[str(dec)]}-{dictionary[str(unit)]}"

    # 100 to 999
    if len(big_value) == 3:
        rest = math.floor(value % 100)

        if rest == 0:
            return f'{dictionary[big_value[0]]} {_CENTS_}'

        return f'{dictionary[big_value[0]]} {_CENTS_} and {number_to_word(rest)}'

    # up to 1000
    if value == 1000:
        return f'{dictionary[big_value[0]]} {_MILLS_}'

    raise AttributeError('Invalid value')
