# - - кодировка: utf-8 - -
A = int(input())
B = int(input())
if A < B:
    for t in range(A, B +  1):
        print(t, end =' ')
else:
    for t in range(A, B - 1, -1):
        print(t, end =' ')

