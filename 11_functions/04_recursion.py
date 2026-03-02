'''
 0 1 2 3 5 8 13
 1 2 3 4 5 6  7....
 # fibonacci sequence
 fib(0) = 0
 fib(1) = 1
 fib(2) = fib(0) + fib(1)
 fib(3) = fib(1) + fib(2)
 fib(4) = fib(2) + fib(3) # This not a function.
 fib(n) = fib(n-1) + fib(n-2)
'''
def fib(n):
    # Base case of recursion
    if (n == 0 or n == 1):
        return n
    
    return fib(n - 1) + fib(n - 2)  # Recursive case    
print(fib(6))  # Output: 8

# fib(4)+fib(5)
# fib(2)+fib(3) + fib(5)
# fib(0)+fib(1)+fib(3)+fib(5) 
# 0+1+fib(1)+fib(2)+fib(3)+fib(4)
# 0+1+1+0+1+1+fib(0)+fib(1)+fib(2) + fib(3) 
# 0+1+1+0+1+1+0+1+fib(0) + fib(1) + fib(3)
# 0+1+1+fib(0)+fib(1)+fib(1)+fib(2)+fib(4) 
# 0+1+1+0+1+1+0+1+0+1+fib(1)+fib(2)
# 0+1+1+0+1+1+0+1+0+1+1+fib(0)+fib(1)
# 0+1+1+0+1+1+0+1+0+1+1+0+1 # output: 8






