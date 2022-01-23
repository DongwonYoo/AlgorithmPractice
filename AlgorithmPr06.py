#GreedyAlgorithm
#毎時最善の場合だけ取り出す
#他の場合は考えない。
#全ての場合を見ないのでBruteforceより早い
#boj.kr/11047
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins: 
    ans += K // coin
    K %= coin

print(ans)