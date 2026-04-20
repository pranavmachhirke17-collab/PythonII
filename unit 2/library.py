class library:
    def __init__(self,book_name,author):
        self.book_name = book_name
        self.author = author
    
    def availability(self,book_name):
        print(f"The book '{book_name}' is available in the library.")

my_book = library("Rich dad poor dad", "Robert kiyosaki")
my_book.availability("Rich dad poor dad")