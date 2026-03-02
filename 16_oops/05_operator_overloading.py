class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_Point(self):
        print(f"X is {self.x} and Y is {self.y}")

    # def __add__(self, p):
    #     return Point((self.x + p.x), (self.y + p.y)) # This is a Extra method to print.
    
p1 = Point(3, 2)  
p2 = Point(6, 4)

p = p1.sum(p2) # Returns a new point which is sum of p1 and p2
# p = p1 + p2 # We overloaded the + Operator by writing __add__ function # Here it is.
p.print_Point()
print(dir(p1))
