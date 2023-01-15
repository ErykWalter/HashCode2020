from Library import Library
from Problem import Problem

class ProblemStupidGreedy(Problem):
    def solve(self):
        self.libraries_order = sorted(self.all_libraries, key=lambda x: x.get_score(self.num_of_days), reverse = True)
        
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