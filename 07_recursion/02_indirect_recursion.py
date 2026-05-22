def a(n):
    if n > 0:
        print(n)
        return b(n - 1)

def b(n):
    if n < 1:
        return n
    else:
        print(n)
        n = n - 1
        return a(n)

a(5)