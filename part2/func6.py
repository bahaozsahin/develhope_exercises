def fib(n):
    if n in {0,1}:
        return n        #for 0. and 1. state it is 0 and 1 respectively
    return fib(n-1) + fib(n-2)  #recursion

fib_list = [fib(n) for n in range(5)]
print(fib_list)