#boj.kr/1302
#一番売れた本の名前を出力
d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())
candi = []
for k, v in d.items():
    if v == m:
        candi.append(k)
        6

candi.sort()

print(candi[0])
        
# d.keys()
# d.values()
# d.items()