# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-08-31 18:32:22
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-914043-1-1.html

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


def k_smallest_substr(s, k):
    n = len(s)
    l = 0
    r = 0
    cnt = 0
    mn = float("inf")
    res = None
    while r < n:
        if s[r] == "1":
            cnt += 1
        if cnt < k:
            r += 1
        else:
            while s[l] == "0":
                l += 1
            cur_len = r - l + 1
            if cur_len < mn or (cur_len == mn and s[l : r + 1] < res):
                mn = cur_len
                res = s[l : r + 1]
            cnt -= 1
            l += 1
            r += 1
    return res if res else "-1"


def solve():
    s = ins()
    k = inp()
    return k_smallest_substr(s, k)


t = 1
while t:
    t -= 1
    print(solve())
