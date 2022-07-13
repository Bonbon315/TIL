n = int(input(), 16)

i = 1
while i<=15:
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
    i += 1
