# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-02 12:19:44
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-1012927-1-1.html

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


def countSubstrings(input_str: str) -> int:
    length = len(input_str)
    string_int = {"a": 1, "b": 1}
    for i in range(2, 26):
        string_int[chr(ord("a") + i)] = (i - 2) // 3 + 2
    extraordinary = 0
    for i in range(length):
        string_sum = 0
        for j in range(i, length):
            string_sum += string_int[input_str[j]]
            if not string_sum % (j - i + 1):
                extraordinary += 1
    return extraordinary


def solve():
    s = ins()
    return countSubstrings(s)


t = 1
while t:
    t -= 1
    print(solve())
