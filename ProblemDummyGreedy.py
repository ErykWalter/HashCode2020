from Library import Library
from Problem import Problem

class ProblemDummyGreedy(Problem):
    def solve(self):
        self.libraries_order = sorted(self.all_libraries, key=lambda x: x.get_score(self.num_of_days), reverse = True)