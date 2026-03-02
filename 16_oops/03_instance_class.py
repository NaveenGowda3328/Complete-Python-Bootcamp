class Employee:
    company = "Asus"
    def __init__(self,salary, name, bond, company):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    # def get_info(self):
    #     print(f"The name of the employee is {self.name}, Salary is {self.salary}, The bond is for {self.bond} years")

e1 = Employee(3000,"Naveen",1,"Tesla")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company)

# Oject introspection
print(dir(e1)) 
