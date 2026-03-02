# Decorators is a functin that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function.
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper
@decorator  # we do this and we get same output.
def say_hello():
    print("Hello!")

say_hello()
# f = decorator(say_hello) # instead of doing this.
# f()
'''
f will something looks like this 
def f():
    print("I am about to execute a function....")
    print(Hello!)
    print("I have executed this function....")
'''



