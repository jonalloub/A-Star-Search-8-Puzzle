from Problem import Problem
from SearchAgent import astar_search

# from SearchAgent import iterative_deepening_search

# Prompting user for input and saving it as initial
initial = input("\nPlease enter an Initial State XXXXXX and press enter: ")

# Defining goal state
goal = ["1","2","3","4","5","6", "7", "8", "0"]

# Defining the problem with the initial value entered
problem = Problem(list(initial), goal)

# Letting user know what the goal state is
print("\nThe Goal State is 123456780")

# Performing the search
result = astar_search(problem)

# Printing the result
printOut = result.solution()
print('-'.join(str(i) for i in printOut))
