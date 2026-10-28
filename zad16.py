import sys
sys.setrecursionlimit(10**6)
def g(n):
    if n<=25:
        return 2*(n+1)
    else:
        return g(n-4)+n
def f(n):
    return g(n-1)-g(n-5)
print(f(150774))
# ПАМЯТКА
# Если написано f(n) = 1, то будет
# if n == 1:
# return 1
# и как показано на примере, нужно делать последовательно, если в f есть g, то g идёт первей