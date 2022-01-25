#https://www.acmicpc.net/problem/8958
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for i in ox_list:
        if i == 'O':
            score += 1
            sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)

