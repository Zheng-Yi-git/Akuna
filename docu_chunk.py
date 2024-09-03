# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-08-31 18:20:35
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


def document_chunk(totalPackets, uploaded):
    # e.g. (5, [[1, 2]])
    uploaded.sort(key=lambda x: x[0])
    uploaded.append([totalPackets + 1, totalPackets + 1])
    last_end = 0
    res = 0
    for start, end in uploaded:
        res += bin(start - last_end - 1).count("1")
        last_end = end
    return res


def solve():
    tot = inp()
    n = inp()
    uploaded = []
    for _ in range(n):
        uploaded.append(inlt())
    return document_chunk(tot, uploaded)


t = 1
while t:
    t -= 1
    print(solve())
