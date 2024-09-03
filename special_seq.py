# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-02 12:32:19
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-1021608-1-1.html

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


def do_query(q):
    dp = [""] * 55
    dp[1] = "1"
    for i in range(2, 55):
        prev = dp[i - 1]
        curr = ""
        j = 0
        while j < len(prev):
            count = 1
            while j + 1 < len(prev) and prev[j] == prev[j + 1]:
                count += 1
                j += 1
            curr += str(count) + prev[j]
            j += 1
        dp[i] = curr
    for i in range(55):
        dp[i] = sum([int(x) for x in dp[i]])
        with open("./111.txt", "a") as f:
            f.write(str(dp[i]) + "\n")
    res = []
    n = len(q)
    for i in range(n):
        res.append(dp[q[i]])
    return res


def solve():
    q = inlt()
    return do_query(q)


t = 1
while t:
    t -= 1
    print(*solve())
