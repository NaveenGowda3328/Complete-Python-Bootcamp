a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
   raise ValueError("Please dont divide by 0")

print(f"The division is {a / b}")

