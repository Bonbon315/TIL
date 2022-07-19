number = int(input())

a = []
for i in str(number):
    a.append(i)
b = list(map(int, a))
result = sum(b)
print(result)