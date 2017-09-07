class Problem(object):
    """Representation of a problem"""

    def __init__(self, initial, goal):
        self.initial = list(initial)
        self.goal = list(goal)

    def actions(self, state):
        """Returns possible actions on current state"""
        actions_list = []
        index_of_blank_space = state.index("0")

        # The four possible actions Up, Down, Left and Right
        # can only be done if the blank space is in a certain space
        if index_of_blank_space == 0 or index_of_blank_space == 1 \
                or index_of_blank_space == 2 or index_of_blank_space == 3 \
                or index_of_blank_space == 4 or index_of_blank_space == 5:
            actions_list.append("U")

        if index_of_blank_space == 3 or index_of_blank_space == 4 \
                or index_of_blank_space == 5 or index_of_blank_space == 6 \
                or index_of_blank_space == 7 or index_of_blank_space == 8:
            actions_list.append("D")

        if index_of_blank_space == 7 or index_of_blank_space == 6 \
                or index_of_blank_space == 4 or index_of_blank_space == 3 \
                or index_of_blank_space == 1 or index_of_blank_space == 0:
            actions_list.append("L")

        if index_of_blank_space == 8 or index_of_blank_space == 7 \
                or index_of_blank_space == 5 or index_of_blank_space == 4 \
                or index_of_blank_space == 2 or index_of_blank_space == 1:
            actions_list.append("R")

        return actions_list

    def result(self, state, action):
        """Returns resulting state after a certain action"""
        # Has not taken in account false moves

        wState = list(state)

        index_of_blank_space = state.index("0")

        if action == "L":
            wState[index_of_blank_space], wState[index_of_blank_space + 1] \
                = wState[index_of_blank_space + 1], wState[index_of_blank_space]

        if action == "R":
            wState[index_of_blank_space], wState[index_of_blank_space - 1] \
                = wState[index_of_blank_space - 1], wState[index_of_blank_space]

        if action == "U":
            wState[index_of_blank_space], wState[index_of_blank_space + 3] \
                = wState[index_of_blank_space + 3], wState[index_of_blank_space]

        if action == "D":
            wState[index_of_blank_space], wState[index_of_blank_space - 3] \
                = wState[index_of_blank_space - 3], wState[index_of_blank_space]


        return wState

    def path_cost(self,cost):
        return cost + 1


    def goal_test(self, state):
        """Returns boolean whether the goal state has been reached"""
        if state == self.goal:
            return True
        else:
            return False
