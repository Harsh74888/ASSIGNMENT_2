# create a class name student with attributes name,age and grade.
# Implement a method to display the student's information in a formatted string
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
S1=Student("harsh",21,"A")
S2=Student("om",22,"B")
print(S1.name)
print(S1.age)
print(S1.grade)
print(S2.name)
print(S2.age)
print(S2.grade)
