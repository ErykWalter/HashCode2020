import random

class Library:
    """It's a class which represents given library"""
    def __init__(self, idx : int, num_of_books : int, days_to_signup : int, books_per_day : int):
        self.id = idx
        self.num_of_books = num_of_books
        self.days_to_sign_up = days_to_signup
        self.books_per_day = books_per_day
        self.book_ids = set()
        self.book_order = list()
        self.score = 0
    
    def set_book_ids(self, book_ids):
        self.book_ids = book_ids
        self.book_order = list(book_ids.keys())
        
    def update_book_ids(self, books_to_delete : set):
        common_books = self.book_ids.keys() & books_to_delete
        self.book_ids = dict(filter(lambda key: key not in common_books, self.book_ids.items()))
        
    def __str__(self):
        return f"LibID: {self.id};\nSignup: {self.days_to_sign_up},\nBooks_per_day: {self.books_per_day},\nBooks: {self.book_ids}\n"
    
    def get_score(self, last_day : int, start_day = -1, books_to_delete = set()) -> int:
        if (start_day < self.days_to_sign_up):
            start_day = self.days_to_sign_up
        if (self.score == 0):
            values = [val for i, val in enumerate(self.book_ids.values()) if i < (last_day - start_day) * self.books_per_day]
            self.score = sum(values)
        else:
            common_books = self.book_ids.keys() & books_to_delete
            diff = sum(self.book_ids[i] for i in common_books)
            # self.book_ids -= common_books
            self.score -= diff
        return self.score
    
    def get_output(self, last_day, start_day = -1) -> str:
        if (start_day < self.days_to_sign_up):
            start_day = self.days_to_sign_up
        
        bound = (last_day - start_day) * self.books_per_day
        text = f"{self.id} {min(bound, len(self.book_ids))}\n"
        
        for i, idx in enumerate(self.book_order):
            if i >= bound:
                break
            text += (str(idx) + " ")
        text += "\n"
        return text
    
    def get_scanned_books(self, last_day, start_day = -1) -> set:
        if (start_day < self.days_to_sign_up):
            start_day = self.days_to_sign_up
            
        if (start_day > last_day):
            return set()
            
        bound = (last_day - start_day) * self.books_per_day
        return set(self.book_order[:bound])
    
    def get_random_books(self, last_day, start_day = -1):
        random.shuffle(self.book_order)
        return set(self.book_order[:(last_day - start_day) * self.books_per_day])
        