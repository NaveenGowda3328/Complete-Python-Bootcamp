s = {5,6,4,2,4,55,623,}
print(s)
s.add(1)
print(s)
s.remove(623)
print(s)
# s.remove(10000)# This will raise an error because 10000 is not in the set.
s.discard(10000) # This will not raise an error, it will simply do
s.pop() # # This will remove and return an arbitrary element from the set.
print(s)