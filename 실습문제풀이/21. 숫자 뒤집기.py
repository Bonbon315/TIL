number = int(input())

while number > 0:
    print(number%10, end='')
    number //= 10