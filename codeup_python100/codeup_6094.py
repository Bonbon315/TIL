n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])

fast = k[0]

for i in k:
    if i < fast:
        fast = i

print(fast)