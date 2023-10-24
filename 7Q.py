# a class name Book with attributes title,author and price.
# implement a method to display the book information and 
# apply a discount on the price also implement a subclass named EBook
#  with an additional attributes format override the display method for the Ebook subclass 
class Book:
    def __init__(self,title, author, price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
    def discount(self,dis):
        if 0<dis<100:
            self.price-=self.price*(dis/100) 
            print("the given discount:",dis)
            print("new price:",self.price)
class Ebook(Book):
    def __init__(self,title, author, price,format):
        super().__init__(title,author,price)
        self.format=format
    def display(self):
        super().display()
        print("formate:",self.format) 
book1 = Book("Half girlfrienf ", "chetan bhagat", 500)
print("Regular Book Information:")
book1.display()
book1.discount(10)

#  e-book
ebook1 = Ebook("Python for Beginners", "John Smith", 200, "PDF")
print("\nE-Book Information:")
ebook1.display()
ebook1.discount(20)           
