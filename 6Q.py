# write a python program to create a class name car with attributes 
# models color and price implement method to start ,stop and accelerate the car.
# also implement a static method to count the number of cars created. 
class Car:
    car_count=0   
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
        self.speed=5
        Car.car_count+=1
    def start (self):
            if self.speed==0:
                print(f"the {self.color} {self.model} has started")
            else:
                 print(f"the{self.color}{self.model} already running")
    def stop(self):
            if self.speed==0:
            
             print(f"The {self.color} {self.model} is already stopped.")
            else:
             print(f"The {self.color} {self.model} has stopped.")
             self.speed = 0
    def accelerate(self, speed_increase):
            if speed_increase > 0:
              self.speed += speed_increase
              print(f"The {self.color} {self.model} is now moving at {self.speed} mph.")
            else:
              print("Speed increase must be greater than 0.")

    @staticmethod
    def get_car_count():
     return Car.car_count

# Creating car objects
car1 = Car("Toyota Camry", "Blue", 25000)
car2 = Car("Honda Accord", "Red", 27000)
car3 = Car("tata","black",100000)
# Starting and accelerating the first car
car1.start()
car1.accelerate(30)

# Stopping the first car
car1.stop()

# Starting the second car
car2.start()

# Printing the total number of cars created
print(f"Total number of cars created: {Car.get_car_count()}")





     

