H, M = map(int, input().split())
cooktime = int(input())

time = H*60 + M
time += cooktime

if time >= 1440:
    time -= 1440

H = time // 60
M = time % 60

print(H, M)