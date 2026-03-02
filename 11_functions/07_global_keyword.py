def sum(a,d):
    print("Hey I am summing")
    c = a + d
    global z  # please modify global z
    z = 1 # This will refer to global z and create a local variable
    return c
z = 100  
print(sum(5,15))  # Output: 20
print(z) # Output: 1