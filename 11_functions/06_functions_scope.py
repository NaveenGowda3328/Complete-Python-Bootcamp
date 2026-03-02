def sum(a,b):
    # a and b are local variables.
    c = a + b
    z = 1 # It creates a local variable called z wich is destroyed after this function returns.
    return c

def greet():
    z = 32 # Local variable, Why because it is inside the greet function.
print("Hello")  # This function prints a greeting

z = 8 # z is a global variable    
print(z)
print(sum(5, 5))  # Output: 10
# print(z)

# greet()  # Output: Hello

