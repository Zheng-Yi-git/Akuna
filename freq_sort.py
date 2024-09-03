# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-02 12:14:09
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-1022809-1-1.html

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


from collections import Counter


def freq_sort(arr):
    cnt = Counter(arr)
    return sorted(arr, key=lambda x: (cnt[x], x))


def solve():
    a = inlt()
    return freq_sort(a)


t = 1
while t:
    t -= 1
    print(*solve())
