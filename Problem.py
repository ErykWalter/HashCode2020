class Problem:
    def __init__(self, num_of_books : int, num_of_libraries : int, num_of_days : int, book_values = [] : list):
        self.num_of_books = num_of_books
        self.num_of_libraries = num_of_libraries
        self.num_of_days = num_of_days
        self.book_values = book_values
        self.already_scanned_books = set()
        self.already_scanned_libraries = set()
        self.all_libraries = set()
        self.libraries_order = list()
        
    def set_book_values(book_values : list):
        self.book_values = book_values