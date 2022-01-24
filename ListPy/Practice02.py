#MaxIndex
#Maxindex
import sys
input = sys.stdin.readline
numList =[]
for _ in range(9):
    i = int(input())
    numList.append(i)
print(max(numList))
print(numList.index(max(numList))+1)
