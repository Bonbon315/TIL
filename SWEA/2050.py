import sys
sys.stdin = open("2050_input.txt", "r")

T = input()

for letter in T:
    temp = ord(letter) - 64
    print(temp, end=' ')