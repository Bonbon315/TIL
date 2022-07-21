import sys
sys.stdin = open("1976_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    H1, M1, H2, M2 = map(int, input().split())

    minute = M1 + M2
    hour = H1 + H2
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour >= 13:
        hour -= 12
    
    print(f'#{test_case} {hour} {minute}')
