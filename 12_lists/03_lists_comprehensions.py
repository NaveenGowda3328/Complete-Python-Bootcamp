# creae a list contianing the table of 5.
# a = [5]
table = []
for i in range(1,11):
    table.append(5* i) #a[0]*i
print(table)  # This will print the table of 5.
# Shorter way to create the same list using list comprehension.
table = [x ** 2 for x in range(5)]   
print(table)  