from math import radians
#https://www.acmicpc.net/problem/2577
#Count

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = list(str(a * b * c))
for i in range(10):
    print(d.count(str(i)))
