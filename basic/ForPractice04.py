#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#https://www.acmicpc.net/problem/11021
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    c = a +b
    print("Case #%s: %s"%(i+1, c ))
