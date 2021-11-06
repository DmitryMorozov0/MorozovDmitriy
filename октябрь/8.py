# - - кодировка: utf-8 - -
n = int(input())     #n<=9
for i in range(1, n + 1):
    for t in range(1, i + 1):
        print(t, end='')
    print()