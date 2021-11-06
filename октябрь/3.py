# - - кодировка: utf-8 - -
A = int(input())
B = int(input())
# A > B
if A % 2 == 0:
    for t in range(A - 1, B - 1, - 2):
        print(t, end =' ')
else:
    for t in range(A, B - 1, - 2):
        print(t, end =' ')