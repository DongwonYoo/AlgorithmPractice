# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
#https://www.acmicpc.net/problem/11022

import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b =map(int,input().split())
    c = a+b
    print("Case #%s: %s + %s = %s"%(i+1, a, b, c))