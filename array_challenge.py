# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-01 23:54:39
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-1083866-1-1.html

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


def array_challenge(n, a):
    res = [0]
    sm = a[0]
    for i in range(1, n):
        res.append(a[i] * i - sm)
        sm += a[i]
    return res


def solve():
    n = inp()
    a = inlt()
    return array_challenge(n, a)


t = 1
while t:
    t -= 1
    print(*solve())
