#https://www.acmicpc.net/problem/4344

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    nums = list(map(int,input().split()))
    avg =sum(nums[1:])/nums[0] #平均を求める
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1       #平均を超える人の人数を求める
    rate = cnt/nums[0]*100 #平均を超える人の割合を求める
    print(f'{rate:.3f}%')
    