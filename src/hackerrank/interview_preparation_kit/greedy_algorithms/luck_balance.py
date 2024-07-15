# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/luck-balance.md]] # noqa
# pylint: enable=line-too-long

# pylint: disable=too-few-public-methods
class Contest:
    luck = 0
    important = 0

    def __init__(self, luck, important):
        self.luck: int = luck
        self.important: int = important

    def __getitem__(self, item):
        return self.__dict__[item]


def luck_balance(k, contests: list) -> int:

    important_contests: list[Contest] = []
    nonimportant_contests: list[Contest] = []

    for contest in contests:
        luck = contest[0]
        important = contest[1]

        if important == 1:
            important_contests.append(Contest(luck=luck, important=important))
        else:
            nonimportant_contests.append(Contest(luck=luck, important=important))

    important_contests = sorted(
        important_contests,
        key=lambda contest: (-contest['important'], -contest['luck'])
    )

    total: int = 0
    size: int = len(important_contests)
    cut: int = min(k, size)

    for i in range(0, cut):
        total += important_contests[i].luck

    for i in range(cut, size):
        total -= important_contests[i].luck

    for contest in nonimportant_contests:
        total += contest.luck

    return total
