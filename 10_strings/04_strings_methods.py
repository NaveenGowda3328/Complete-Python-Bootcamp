# name = "Naveen" # string is immutable
# # print[0] = "R" # You cannot do this 
# a = len(name)
# print(a) # Length of the string

s = "hello world"
a = len(s)
# print(a) # Length of the string
# print(s.upper()) # Convert to uppercase
# print(s.lower()) # Convert to lowercase
# print(s.title()) # Convert to title case
# print(s.capitalize()) # Capitalize the first letter

# text = "  hello world  "
# print(text.strip())  # Output: "hello world"
# print(text.lstrip())  # Output: "hello world  "
# print(text.rstrip())  # Output: "  hello world"

# text = "Python is fun and fun and fun"
# print(text.find("is")) # Output: 7 # Index of first occurrence of "is"
# print(text.replace("fun", "awesome")) # Output: "Python is awesome and awesome and awesome"

# text = "Apple, Banana, Cherry"
# print(text)
# print(text.split(", ")) # Output: ['Apple', 'Banana', 'Cherry'] 
# print(",".join(["Orange", "Grapes"])) # Output: "Apple, Banana, Cherry, Orange, Grapes"
# print(text.count("a")) # Output: 3 # Count occurrences of "a"

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False




