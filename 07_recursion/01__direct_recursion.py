def direct_recursion(n):
    if n < 1:
        return n
    
    print(n)
    return direct_recursion(n - 1)

direct_recursion(5) # start the program