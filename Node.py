from Problem import Problem

class Node(object):
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.action = action
        self.state = list(state)
        self.parent = parent
        self.path_cost = path_cost

    def __repr__(self):
        return "Node {}".format(self.state)

    def __lt__(self, node):

        return self.state < node.state
    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, self, action, problem.path_cost(self.path_cost + 1))

    def solution(self):
        """Returns the solution, the sequence of actions it took to get to this node"""

        node, path_back = self, []

        while node:
            if node.action is not None:
                path_back.append(node.action)
            node = node.parent

        return list(reversed(path_back))



