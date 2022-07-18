# numbers = input().split()
# print(sum(numbers))

# numbers 가 str이기때문에 나는 오류.

numbers = map(int, input().split())
print(sum(numbers))
