#!/usr/bin/env python

from Problem import Problem
from ProblemStupidGreedy import ProblemStupidGreedy
from input_parser import parse
from Library import Library
from ProblemImprovedGreedy import ProblemImprovedGreedy

def main():
    problem = parse(ProblemImprovedGreedy)
    problem.solve()
    problem.output()
    
if __name__=="__main__":
    main()