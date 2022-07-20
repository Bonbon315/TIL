import sys
sys.stdin = open("1986_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    temp = 0
    for number in range(1, N + 1):
        if number%2 == 1:
            temp += number
        else:
            temp -= number
    print(f'#{test_case} {temp}')
