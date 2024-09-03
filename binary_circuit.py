# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-03 10:53:31
# ----------------------------------------------

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


def maxOperations(self, s: str) -> int:
    cnt = 0
    ones = 0
    last_is_one = False
    for i, x in enumerate(s):
        if x == "0":
            if last_is_one:
                cnt += ones
                last_is_one = False
        else:
            last_is_one = True
            ones += 1
    return cnt


def solve():
    n = inp()
    a = inlt()

    return


t = inp()
while t:
    t -= 1
    solve()
