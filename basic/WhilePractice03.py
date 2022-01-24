
#https://www.acmicpc.net/problem/1110

import sys
input = sys.stdin.readline
N = int(input())#25
nN = N #25
cnt = 0
while True:
    A = nN//10 #2
    B = nN%10 # 5
    C = A + B  #7
    new_num = ((nN%10)*10) + (C%10) #57
    cnt += 1
    
    if N == new_num:
        break
    nN = new_num 
    print(new_num)

print(cnt)