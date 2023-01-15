from Problem import Problem
from Library import Library
from Book import Book


def parse( data : str ) -> Problem:
    lines_of_input = data.split("\n")
    num_of_books, num_of_libs, num_of_days = map(int, lines_of_input[0].split())
    books_values = list(map(int, lines_of_input[1].split()))
    libraries = set()
                         
    for line in range(2, num_of_libs*2 + 2, 2):
        num_of_books_in_lib, signup_time, books_per_day = map(int, lines_of_input[line].split())
        if (signup_time > 
        
        bookIDs = list(set(map(int, lines_of_input[line+1].split())))
        bookIDs.sort(key = lambda x: books_values[x], reverse = True)
        
        bookIDs = {key:books_values[key] for key in bookIDs}
        lib = Library(line //2 -1, num_of_books_in_lib, signup_time, books_per_day)
        lib.set_book_ids(bookIDs)
        libraries.add(lib)
        
    return Problem(num_of_books, num_of_libs, num_of_days, books_values, libraries)

def test():
    data = """6 2 7
1 2 3 6 5 4
5 2 2
0 1 2 3 4
4 3 1
3 2 5 0"""
    problem = parse(data)
    print(problem)    
    
if __name__ == "__main__":
    test()