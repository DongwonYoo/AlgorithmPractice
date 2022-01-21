#boj.kr/9012
#Last in firs out
#正しい組を探す問題はStack

T =int(input())
for i in range(T):
    isVPS = True
    stk = []
    for ch in input():
        if ch =='(':
            stk.append(ch)
        else:
            if len(stk) > 0: #stkが空いてるか確認
                stk.pop()
            else:
                isVPS = False
                break

    if len(stk) > 0:
        isVPS = False

    print('YES' if isVPS else 'NO')
            