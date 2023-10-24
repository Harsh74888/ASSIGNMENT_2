# write a python program to create a class name employee with attributes names id and salary. 
# implement method to get and set the salary of employee also 
# implement a class method to claculate he average salary of all the employees 
class Employee:
    total_salary = 0
    total_employees = 0

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.total_salary += salary
        Employee.total_employees += 1

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        Employee.total_salary -= self.salary
        self.salary = new_salary
        Employee.total_salary += new_salary

    @classmethod
    def average_salary(cls):
        if cls.total_employees == 0:
            return 0
        return cls.total_salary / cls.total_employees

employee1 = Employee("ram", 101, 100)
employee2 = Employee("om", 102, 800)

print(f"{employee1.name}'s salary: RS{employee1.get_salary()}")
print(f"{employee2.name}'s salary: Rs{employee2.get_salary()}")

employee2.set_salary(500)
print(f"{employee2.name}'s updated salary: RS{employee2.get_salary()}")

print(f"Average salary of all employees: Rs{Employee.average_salary()}")

