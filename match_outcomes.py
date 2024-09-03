# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-01 23:22:36
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-937372-1-1.html

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


def calc_diff(seq):
    l = 0
    r = len(seq) - 1
    n = len(seq)
    cur = "l"
    first = 0
    second = 0
    for i in range(n):
        if i % 2 == 0:
            if cur == "l":
                first += seq[l]
                if seq[l] % 2 == 0:
                    cur = "r"
                l += 1
            else:
                first += seq[r]
                if seq[r] % 2 == 0:
                    cur = "l"
                r -= 1
        else:
            if cur == "l":
                second += seq[l]
                if seq[l] % 2 == 0:
                    cur = "r"
                l += 1
            else:
                second += seq[r]
                if seq[r] % 2 == 0:
                    cur = "l"
                r -= 1
    return first - second


def solve():
    seq = inlt()
    return calc_diff(seq)


t = 1
while t:
    t -= 1
    print(solve())
