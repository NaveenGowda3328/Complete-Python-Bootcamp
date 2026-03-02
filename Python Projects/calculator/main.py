try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of opertion do you want to perfrom.\nPress + for Addition\nPress - for Subtraction\nPress * for Multiplication\nPress / for Division")

    o = input("Enter Opertion: ")
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")

except Exception as e:
    print("Enter valid value of a and b")

# print(int(eval(input("Enter the calculation: "))))