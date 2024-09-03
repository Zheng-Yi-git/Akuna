# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-02 11:49:14
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


global_tag = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def assign_tag(row, col, arr):
    global global_tag
    for i in range(row):
        for j in range(col):
            if arr[i][j] not in ["a", "b", "c"]:
                continue
            else:
                # bfs
                queue = [(i, j)]
                cur_tag = arr[i][j]
                while queue:
                    x, y = queue.pop(0)
                    arr[x][y] = global_tag
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < row and 0 <= ny < col and arr[nx][ny] == cur_tag:
                            queue.append((nx, ny))
                global_tag += 1
    return


def solve():
    rows, cols = invr()
    row_array = []
    for _ in range(rows):
        row_array.append(insr())
    assign_tag(rows, cols, row_array)
    return global_tag


t = 1
while t:
    t -= 1
    print(solve())
