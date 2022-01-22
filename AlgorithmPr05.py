#Bruteforce(全ての場合の数を探索して認める結果を得る)
#Permutation  全ての場合の数を順番に見る時
#Combination順番に関係なく
#boj.kr/2309
from itertools import combinations

height = [int(input()) for _ in range(9)]
for combi in combinations(height, 7):#名前と取り出す個数
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)

        break #正解が二つ以上の場合

#多重for文でもできる