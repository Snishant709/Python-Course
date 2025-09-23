class Library:
    books=["Comics","Story","Wealth","Bravery"]
    no_books=len(books)
    
    def show(self):
        print(f"The books we have is {self.books} and count is {self.no_books}")
obj1=Library()
obj1.show()
print(obj1.books.append("Novel"))
obj1.show()


