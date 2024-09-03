# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-03 10:35:27
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


def get_max_distinct(a, b, k):
    n = len(a)
    duplicates_in_a = 0
    unique_in_b = 0
    s = set()
    s2 = set()
    for num in a:
        if num in s:
            duplicates_in_a += 1
        else:
            s.add(num)
    for num in b:
        if num not in s and num not in s2:
            unique_in_b += 1
            s2.add(num)
    return n - duplicates_in_a + min(duplicates_in_a, unique_in_b, k)


def solve():
    k = inp()
    a = inlt()
    b = inlt()
    return get_max_distinct(a, b, k)


t = 1
while t:
    t -= 1
    print(solve())
