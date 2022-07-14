word = input()

aeiou = 0
for i in word:
    if i=='a' or i=='e' or i =='i' or i=='o' or i=='u':
        aeiou += 1

print(aeiou)