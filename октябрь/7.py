# - - кодировка: utf-8 - -
n = int(input())
f = 1
sum = 0            #сумма
for t in range(1, n + 1):
    f = f * t
    sum = sum + f
print(sum)
