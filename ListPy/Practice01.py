#https://www.acmicpc.net/problem/10818
import sys
input =sys.stdin.readline
A = int(input())
B = list(map(int,input().split()))
print(min(B),max(B))

#sort
#B.sort
#print(B[0],B[-1])