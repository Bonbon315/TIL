H, M = map(int, input().split())

time = H*60 + M
if time < 45:
    time += 1440
time -= 45

H = time // 60
M = time % 60

print(H, M)