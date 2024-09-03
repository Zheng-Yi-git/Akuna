# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-01 23:41:15
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


from bisect import bisect_left, bisect_right


def count_pairs(n, profit, cost):
    net = [profit[i] - cost[i] for i in range(len(profit))]
    net.sort()
    res = 0
    for i in range(n - 1, -1, -1):
        if net[i] <= 0:
            break
        else:
            # find the first element that is greater than -net[i]
            j = bisect_right(net, -net[i])
            if j >= i:
                break
            else:
                res += i - j
    return res


def solve():
    n = inp()
    profit = inlt()
    cost = inlt()
    return count_pairs(n, profit, cost)


t = 1
while t:
    t -= 1
    print(solve())
