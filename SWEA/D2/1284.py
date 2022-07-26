import sys
sys.stdin = open("1284_input.txt", "r")


T = int(input())
#P = A사 리터당요금
#Q = B사 기본요금
#R = B사 기본요금 범위(L)
#S = B사 리터당 요금
#W = 사용자의 사용량
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    costA = P * W
    if(R >= W):
        costB = Q
    else:
        costB = ((W-R)*S) + Q 
    
   
    print(f'#{test_case} {min(costA, costB)}')

