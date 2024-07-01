# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/greedy_algorithms/luck-balance.md]] # noqa
# pylint: enable=line-too-long

# pylint: disable=too-few-public-methods
class Competition:
    luck = 0
    important = 0

    def __init__(self, luck, important):
        self.luck: int = luck
        self.important: int = important

    def __getitem__(self, item):
        return self.__dict__[item]


def luck_balance(k, contests: list) -> int:

    important_competitions: list[Competition] = []
    nonimportant_competitions: list[Competition] = []

    for contest in contests:
        luck = contest[0]
        important = contest[1]

        if important == 1:
            important_competitions.append(Competition(luck=luck, important=important))
        else:
            nonimportant_competitions.append(Competition(luck=luck, important=important))

    important_competitions = sorted(
        important_competitions,
        key=lambda contest: (-contest['important'], -contest['luck'])
    )

    total: int = 0
    size: int = len(important_competitions)

    for i in range(0, min(k, size)):
        total += important_competitions[i].luck

    for i in range(min(k, size), size):
        total -= important_competitions[i].luck

    for x in nonimportant_competitions:
        total += x.luck

    return total
