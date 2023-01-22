from Problem import Problem
from Library import Library


def parse(classType ) -> Problem:
    """This method reads the input file and returns a problem with all nessasary data to operate.
    The little optimization is done during parsing, if the number of days needed to sign up is greater than number of available days
    this library won't be processed at all."""
    num_of_books, num_of_libs, num_of_days = map(int, input().split())
    books_values = list(map(int, input().split()))
    libraries = set()
                         
    for lib_id in range(num_of_libs):
        num_of_books_in_lib, signup_time, books_per_day = map(int, input().split())
        if (signup_time > num_of_days-1):
            continue
        
        bookIDs = list(set(map(int, input().split())))
        bookIDs.sort(key = lambda x: books_values[x], reverse = True)
        
        bookIDs = {key:books_values[key] for key in bookIDs}
        lib = Library(lib_id, num_of_books_in_lib, signup_time, books_per_day)
        lib.set_book_ids(bookIDs)
        libraries.add(lib)
        
    return classType(num_of_books, num_of_libs, num_of_days, books_values, libraries)

def test():
    data = """6 2 7
1 2 3 6 5 4
5 2 2
0 1 2 3 4
4 3 1
3 2 5 0"""
    problem = parse(data, Problem)
    print(problem)    
    
if __name__ == "__main__":
    test()