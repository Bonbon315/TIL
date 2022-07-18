# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 저렇게 작성하면 조건문의 결과는 항상 참이 된다.
# 비교연산자가 사용되지 않은 조건문은 0이 아닌이상 항상 참이다.
# (참/거짓) 혹은 참 혹은 참 혹은 참 이런식으로 되는것이다. 
# or은 하나만이라도 참이면 실행된다.
# char == 를 각각 적어주면 해결.

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or \
        char == "o" or char == "u":
        count += 1

print(count)