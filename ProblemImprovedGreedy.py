from Problem import Problem
from copy import deepcopy
import time
import random
import sys

class ProblemImprovedGreedy(Problem):
    def solve(self):
        start = time.time()
        self.libraries_order = sorted(self.all_libraries, 
                                      key=lambda lib: lib.get_score(self.num_of_days)/lib.days_to_sign_up, reverse = True)
        # day = 0
        # for lib in self.all_libraries:
        #     lib.update_book_ids(self.already_scanned_books)
        #     self.already_scanned_books.union(lib.get_scanned_books(self.num_of_days, day))
        #     day += lib.days_to_sign_up
        # best_sol = deepcopy(self)
        # best_eval = best_sol.evaluate()
        # without_imrovement = 0
        # while time.time() - start < 60 * 4.5 and without_imrovement < 10:
        #     self.already_scanned_books = set()
        #     for lib in random.sample(self.all_libraries, min(50, len(self.all_libraries))):
        #         lib.get_random_books(self.num_of_days)
        #     day = 0
        #     for lib in self.all_libraries:
        #         self.already_scanned_books.union(lib.get_scanned_books(self.num_of_days, day))
        #         day += lib.days_to_sign_up
        #     evaluation = self.evaluate()
        #     without_imrovement += 1
        #     if (evaluation > best_eval):
        #         best_sol = deepcopy(self)
        #         best_eval = evaluation
        #         without_imrovement = 0
        #         sys.stderr.write(str(evaluation) + "\n")
        # self = best_sol