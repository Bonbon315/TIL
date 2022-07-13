r, g, b = map(int, input().split())

count = 0
for x in range(r):
    for y in range(g):
        for z in range(b):
            print(x, y, z)
            count += 1
            z += 1
        y += 1
    x += 1

print(count)