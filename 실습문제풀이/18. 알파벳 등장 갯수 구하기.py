word = input().lower()

dic = {}

for i in word:
    dic[i] = 0

for i in word:
    dic[i] += 1

for k, v in dic.items():
    print(k, v)