word = 'apple'

apos = 0
for i in word:
    if i=='a':
        break
    apos += 1

if apos>=len(word):
    print(-1)
else:
    print(apos)