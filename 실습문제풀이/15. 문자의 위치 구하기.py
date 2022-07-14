word = input()

apos = 0
for i in word:
    if i == 'a':
        break
    apos += 1

if apos>=len(word):
    print(-1)
else:
    print(apos)


#추가 문제
word2 = input()

apos2 = 0
for i in word2:
    if i == 'a':
        print(apos2, end=' ')
    apos2 += 1