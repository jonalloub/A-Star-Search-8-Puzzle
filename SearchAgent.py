from queue import PriorityQueue
from Node import Node
from Problem import Problem
import sys


def heuristic(node):
    difference = 0
    goal = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
    compare = zip(node, goal)
    for i, j in compare:
        if i != j:
            difference += 1
    return difference

def score(node):
    return node.path_cost + heuristic(node.state)

def best_first_graph_search(problem):

    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    fringe = PriorityQueue()
    fringe.put((score(node), node))

    explored = set()

    while fringe:
        node_tuple = fringe.get()
        node = node_tuple[1]

       # print(problem.goal_test(node.state))

        if problem.goal_test(node.state):
            return node

        explored.add(tuple(node.state))


        for child in node.expand(problem):

            if tuple(child.state) not in explored \
                    and (score(child), child.state) not in fringe.queue:

                fringe.put((score(child), child))


                #exit()

            elif (score(child), child.state) in fringe.queue:
                incumbent_tuple = fringe.get()


                if score(child) < int(incumbent_tuple[0]):
                    fringe.put(child)

    return None


def astar_search(problem):
    return best_first_graph_search(problem)


