from __future__ import annotations
from typing import List


def matrix(t_n: int, t_m: int, init: int | None) -> List[List[int]]:
    result = []

    for _ in range(0, t_n):
        result.append([init for _ in range(t_m)])
    return result
