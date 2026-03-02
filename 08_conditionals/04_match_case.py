a = int(input("Enter a number between 1 and 10: "))
match a:
  case 1: 
    print("You won $20")
  case 7:  
    print("You won a camera")
  case 10: 
    print("You won a mobile phone")
  case _:
    print("better luck next time")