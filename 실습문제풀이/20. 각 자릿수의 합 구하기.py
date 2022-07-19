number = int(input())

a = []
for i in str(number):
    a.append(i)
b = list(map(int, a))
result = sum(b)
print(result)



number = int(input())
result = 0
for i in str(number):
    result += int(i)
print(result)
