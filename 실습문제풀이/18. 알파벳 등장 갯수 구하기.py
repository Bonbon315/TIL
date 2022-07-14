word = input().lower()

dic = {}
for i in word:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for k, v in dic.items():
    print(k, v)