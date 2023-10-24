# create a class name animal with an abstract method  
# name sound.implement subclass for diferent animals such as dog,cat, cow
#  and overide the sound method for each sub class 
from abc import ABC,abstractmethod
class Animals(ABC):
    def sound(self):
        pass
class Dog(Animals):
    def sound(self):
     return "woo!wooo!"
class Cat(Animals):
    def sound(self):
     return "meow"     
class Cow(Animals):
    def sound(self):
     return "moooooo"
dog=Dog()
cat=Cat()
cow=Cow()
print("dog say:",dog.sound())
print("cat say:",cat.sound())
print("cow say:",cow.sound())


    