T = int(input())

for test_case in range(1, T + 1):
    numbers = []
    numbers = map(int, input().split())
    average = round(sum(numbers) / 10)
    print(f'#{test_case} {average}')
