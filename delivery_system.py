# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-08-31 18:45:00
# ----------------------------------------------

# https://www.1point3acres.com/bbs/thread-1021964-1-1.html

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


from heapq import heapify, heappop, heappush


def delivery_system(n, city_from, city_to, company):
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(zip(city_from, city_to)):
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * n
    visited[company - 1] = True
    priority_queue = [(0, company - 1)]
    res = []
    while priority_queue:
        cur_level, cur_node = heappop(priority_queue)
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                res.append(next_node + 1)
                heappush(priority_queue, (cur_level + 1, next_node))
    return res


def solve():
    n = inp()
    city_from = inlt()
    city_to = inlt()
    company = inp()
    return delivery_system(n, city_from, city_to, company)


t = 1
while t:
    t -= 1
    print(*solve())
