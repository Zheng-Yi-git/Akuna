# ----------------------------------------------
# Author: zhengyi20thu
# Time: 2024-09-01 23:09:02
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


def press_key(s, keypad):
    keypad_mat = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            keypad_mat[i][j] = int(keypad[i * 3 + j])
    dis_mat = [[2] * 9 for _ in range(9)]
    for i in range(9):
        dis_mat[i][i] = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(3):
        for j in range(3):
            for dd in dirs:
                ni, nj = i + dd[0], j + dd[1]
                if 0 <= ni < 3 and 0 <= nj < 3:
                    dis_mat[keypad_mat[i][j] - 1][keypad_mat[ni][nj] - 1] = 1
    n = len(s)
    res = 0
    for i in range(n - 1):
        res += dis_mat[int(s[i]) - 1][int(s[i + 1]) - 1]
    return res


def solve():
    s = ins()
    keypad = ins()
    return press_key(s, keypad)


t = 1
while t:
    t -= 1
    print(solve())
