# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count += 1을 반복문 밖에 적었다. 이러면 count는 항상 1이된다.
# 평균값을 구하려면 몫이 아닌 나눗셈의 값을 써야한다.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)