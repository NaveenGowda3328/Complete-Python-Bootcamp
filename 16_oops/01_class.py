# Class: Class is a blueprint or a template. Eg. From for a Exam that contains name, age, electives,father's name etc.

# Oject: Specific instance created from the template (class). Eg. From which contains the data "john Doe".

class Employee:
    company = "TCS"
    # company1 = "HP"
    def get_salary(self):# self means we put any numbers of Employee it's gets same output of salary.# self is important here because self is the way to reference of the class which is been created. 
        return 30000

e1 = Employee() # An oject of class Employee is created here.
print(e1.get_salary()) # Employee e's get_salary method is called 
print(e1.company)     

# e2 = Employee()
# print(e2.get_salary())
# print(e2.company1)
