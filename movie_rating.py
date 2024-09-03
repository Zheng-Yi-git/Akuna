# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-02 11:13:51
# ----------------------------------------------

# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=1083866&pid=19787849&page=1&extra=#pid19787849

import sys

input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def ins():
    return input().strip()


from functools import lru_cache


def select_movies(ratings):
    n = len(ratings)

    @lru_cache(None)
    def dp(i, can_omit):
        if i == n:
            return 0
        if not can_omit:
            return ratings[i] + dp(i + 1, True)
        return max(ratings[i] + dp(i + 1, True), dp(i + 1, False))

    return max(dp(0, True), dp(1, True))


def solve():
    ratings = inlt()
    return select_movies(ratings)


t = 1
while t:
    t -= 1
    print(solve())
