numbers = [1, 2, 4, 6, 8, 10, 11]

total = 0 
count = 0

for i in range(1, len(numbers)-1):
    total += numbers[i]
    count += 1

print(total // count)