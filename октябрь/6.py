# - - кодировка: utf-8 - -
n = int(input())
def find_factorial(n):
    f=1
    for t in range(1, n+1):
         f = t*f       
    return (f'{n}! = {f}')
f = find_factorial(n)
print(f)