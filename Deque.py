
#Last In Last Out First In First OUT

#Queusの機能を全部使える、早い
#Double-Ended QUEue
from collections import deque

dq = deque()

dq.append(123)#右に入れる
dq.appendleft(456)
dq.appendleft(789) #左に入れる
print(dq)
print(dq.pop())
print(dq.popleft())