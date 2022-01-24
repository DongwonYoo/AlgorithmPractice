#https://www.acmicpc.net/problem/14681
import sys
input =sys.stdin.readline
a, b = map(int, input().split())
if a > 0 and b > 0 :
    print(1)
elif a < 0 and b > 0 :
    print(2)
elif a < 0 and b < 0 :
    print(3)
else:
    print(4)