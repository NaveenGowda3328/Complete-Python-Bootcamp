a = {3,5,6,1,2}
b = {1,2,3,4,5}

c = a.union(b)# Contians all the eelements ina a along with all the elements in b.
print(c)

d = a.intersection(b) # Contains only the elements that are present in as well as b.
print(d)

e = a.difference(b) # Contains elements that are in a but not in b.
print(e)