class Car:
    # name = "xyz"
    # year = 2020

    def __init__(self,name,year):
        self.name = name
        self.year = year

    def display(self):
        print("car name",self.name)

obj = Car("Bugati",2025)
obj.display()


''' Inheritance '''
#single ->
# class Person:
#     def __init__(self,name):
#         self.name = name

# class Employee(Person):
#     def __init__(self,name,salary):
#         self.salary = salary
#         super().__init__(name)


#multiple ->
class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self,name,salary):
        self.salary = salary
        super().__init__(name)

class Job:
    def __init__(self,salary):
        self.salary = salary

class EmployeePersonJob(Employee,Job):
    def __init__(self,name,salary):
        Employee.__init__(self,name,salary)
        Job.__init__(self,salary)

# Multilevel ->
class Manager(EmployeePersonJob):
    def __init__(self,name,salary,department):
        EmployeePersonJob.__init__(self,name,salary)
        self.department = department