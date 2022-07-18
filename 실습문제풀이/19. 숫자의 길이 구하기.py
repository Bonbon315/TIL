from pkg_resources import resource_listdir


number = int(input())

result = 0

while number > 0:
    number = number // 10
    result += 1
if number == 0:
    result = 1

print(result)