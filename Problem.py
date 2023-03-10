class Problem:
    def __init__(self, num_of_books : int, num_of_libraries : int, num_of_days : int, book_values, libraries):
        self.num_of_books = num_of_books
        self.num_of_libraries = num_of_libraries
        self.num_of_days = num_of_days
        self.book_values = book_values
        self.already_scanned_books = set()
        self.already_scanned_libraries = list()
        self.all_libraries = libraries
        self.libraries_order = list()
        
    def __str__(self):
        text = f"Num_of_books: {self.num_of_books},\nNum_of_libraries: {self.num_of_libraries},\nAvailable_days: {self.num_of_days}\n"
        text += f"book_values: {self.book_values}\n"
        for lib in self.all_libraries:
            text += str(lib)
        text += f"{len(self.all_libraries)}"
        return text
        
    def set_book_values(self, book_values : list):
        self.book_values = book_values
        
    def output(self) -> None:
        day = 0
        num_of_libs = 0
        text = ""
        for lib in self.libraries_order:
            if day > self.num_of_days:
                break
            num_of_libs += 1
            text += lib.get_output(self.num_of_days, day)
            day += lib.days_to_sign_up
        print(f"{num_of_libs}", text, sep = "\n")
        
    def evaluate(self):
        return sum(map(lambda idx: self.book_values[idx], self.already_scanned_books))
        