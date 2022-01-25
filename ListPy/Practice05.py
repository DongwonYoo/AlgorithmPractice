#https://www.acmicpc.net/problem/1546

import  sys
input = sys.stdin.readline
N = int(input()) #科目数
test = list(map(int,input().split()))#試験点数
top_score = max(test)#最高点数
new_score = []
for i in test:
    new_score.append(i/top_score*100)
avg = sum(new_score)/N

print(avg)

