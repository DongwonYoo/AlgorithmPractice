from itertools import count


#https://paiza.jp/challenges/488/ready

import sys
input =sys.stdin.readline
a = list(map(int,input().split()))
b = []
c = a.pop(0)
d= []

for i in range(c-1):
    b.append(int(input()))
for _ in range(len(b)):
    d.append(int(a[0] - b.pop(0)))
d.append(int(a[0]))
d = sum(d)
print(a[0]*d)