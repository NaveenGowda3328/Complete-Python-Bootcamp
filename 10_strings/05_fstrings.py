# Strings Formatted with f-strings

template = "Dear {}, You are Good. Take this {}$Bag"
a = "Harry"
a1 = 10000
b = "Laro"
b1 = 2000
c = "Karana"
c1 = 3000
# s1 = template.format(a, a1) # Using format method for formatting # Old way.
# print(s1)
print(f"Dear {b}, You are Good. Take this {b1}$Bag") # Using f-string for formatting # New in Python 3.6+
# s2 = template.format(c, c1)
# print(s2) # old way.