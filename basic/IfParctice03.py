#https://www.acmicpc.net/problem/2884


import sys
input =sys.stdin.readline
h, m = map(int, input().split())
if m < 45 :
    h -= 1
    m = 60 -(45-m)
    if h < 0 :
        h = 23
    print(h, m)
else:
    print(h, m-45)