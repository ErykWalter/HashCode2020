class Library:
    """It's a class which represents given library"""
    def __init__(self, idx : int, num_of_books : int, days_to_signup : int, books_per_day : int):
        self.id = idx
        self.num_of_books = num_of_books
        self.days_to_sign_up = days_to_signup
        self.books_per_day = books_per_day
        self.book_ids = set()
        self.scanning_order = list()
    
    def set_book_ids(self, book_ids):
        self.book_ids = book_ids
        
    def update_book_ids(self, books_to_delete : set):
        self.book_ids.difference_update(books_delete)
        
    def __str__(self):
        return f"LibID: {self.id};\nSignup: {self.days_to_sign_up},\nBooks_per_day: {self.books_per_day},\nBooks: {self.book_ids}\n"
            
        
