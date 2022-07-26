import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = [0] * 10

    count = 1
    while 0 in numbers:
        num = str(N * count)
        for i in range(len(num)):
            numbers[int(num[i])] += 1
        count += 1
    print(f'#{test_case} {num}')