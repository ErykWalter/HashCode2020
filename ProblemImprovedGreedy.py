from Problem import Problem
from copy import deepcopy
import time
import random

class ProblemImprovedGreedy(Problem):
    def solve(self):
        start = time.time()
        self.libraries_order = sorted(self.all_libraries, key=lambda lib:lib.days_to_sign_up)
        for lib in self.all_libraries:
            self.already_scanned_books.union(lib.get_scanned_books(self.num_of_days))
        best_sol = deepcopy(self)
        best_eval = best_sol.evaluate()
        while time.time() - start < 60 * 4.5:
            self.already_scanned_books = set()
            for lib in random.sample(self.all_libraries, 5):
                lib.get_random_books(self.num_of_days)
            day = 0
            for lib in self.all_libraries:
                self.already_scanned_books.union(lib.get_scanned_books(self.num_of_days, day))
                day += lib.days_to_sign_up
            evaluation = self.evaluate()
            if (self.evaluate() > best_eval):
                best_sol = deepcopy(self)
                best_eval = evaluation
        self = best_sol