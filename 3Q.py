# create a class name rectangle with attributes length and width.
# implement method to calculate the area and the perimeter of the rectangle.
# also implement a method to compare two rectangle based on their area
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self): 
        return self.length*self.width 
    def perimeter(self):
        return self.length+self.width
    def compare(self,other_recrtangle):
        if self.area()>other_recrtangle.area():
            return "first rectangle has larger area"
        elif self.area()<other_recrtangle.area(): 
            return "first rectangle has smaller area"
        else :
            return"the rectangles are equal"
R1=Rectangle(6,8)
R2=Rectangle(9,7)
print("area of rectangle:",R1.area())  
print("perimeter of rectangle:",R1.perimeter())              
print("area of  another rectangle:",R2.area())  
print("perimeter of another rectangle:",R2.perimeter())              
comparision_result=R1.compare(R2)
print(comparision_result)

