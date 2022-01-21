#KeyとValueを持っている
#Keyは重複❌　Valueは🆗

m = {}

m["A"] = 10
m["WW"] = 20
m["1W"] = 33
m["sdaW"] = 20
print("size:", len(m)) #len=length


for k in m:
    print(k, m[k])