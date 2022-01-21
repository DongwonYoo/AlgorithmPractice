
#First In Last Out Last In First Out
#StackはウェブブラウザでBACK機能　PythonはListでいい
s=[]
s.append(123)
s.append(456)
s.append(789)
#appendは配列の最後に追加
print ("size:", len(s))
while len(s) > 0:
    #-1番目はいつも最後に入れたもの
    print(s[-1])
    s.pop(-1)

    "123(-3) 456(-2) 789(-1) > 123 456 > 123 "