class Library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0

    def addbooks(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def show(self):
        print(f"Library has total {self.no_of_books} books and books are ")
        for book in self.books:
            print(book)

obj1=Library()
obj1.addbooks("Harry Porter")
obj1.show()

    

  
