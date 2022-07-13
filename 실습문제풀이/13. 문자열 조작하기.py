word = input()
result = ''

length = len(word) - 1

while length >= 0:
    result += word[length]
    length -= 1
    
print(result)