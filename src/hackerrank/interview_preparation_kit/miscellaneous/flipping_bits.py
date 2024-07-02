# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/miscellaneous/flipping-bits.md]] # noqa
# pylint: enable=line-too-long

def flipping_bits(number: int) -> int:
    # print(n)

    n_bin = bin(number)
    n_bin_str = str(n_bin).replace("0b", '').rjust(32, "O")
    # print(f'{n_bin_str} lenght is {len(n_bin_str)}')

    result_bin_str = ''
    for bin_digit in n_bin_str:
        if bin_digit == '1':
            result_bin_str = result_bin_str + '0'
        else:
            result_bin_str = result_bin_str + '1'

    # print(f'{result_bin_str} response length is {len(result_bin_str)}')
    return int(result_bin_str, 2)
