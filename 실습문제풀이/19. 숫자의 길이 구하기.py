number = int(input())

result = 0

if number == 0:
    result = 1
while number > 0:
    number = number // 10
    result += 1


print(result)