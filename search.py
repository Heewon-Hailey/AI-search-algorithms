# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    A sample depth first search implementation is provided for you to help you understand how to interact with the problem.
    """
    
    mystack = util.Stack()
    startState = (problem.getStartState(), '', 0, [])
    mystack.push(startState)
    visited = set()
    while mystack :
        state = mystack.pop()
        node, action, cost, path = state
        if node not in visited :
            visited.add(node)
            if problem.isGoalState(node) :
                path = path + [(node, action)]
                break;
            succStates = problem.getSuccessors(node)
            for succState in succStates :
                succNode, succAction, succCost = succState
                newstate = (succNode, succAction, cost + succCost, path + [(node, action)])
                mystack.push(newstate)
    actions = [action[1] for action in path]
    del actions[0]
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def enforcedHillClimbing(problem, heuristic=nullHeuristic):
    """COMP90054 your solution to part 1 here """
    startNode = problem.getStartState()
    initState = (startNode, '', 0, [])
    node, action, cost, path = initState

    while not problem.isGoalState(startNode):
        myqueue = util.Queue()
        visited = set()
        currentState = (startNode, action, cost, path)
        myqueue.push(currentState)
        while not myqueue.isEmpty():
            state = myqueue.pop()
            node, action, cost, path = state
            if node not in visited:
                visited.add(node)
                if heuristic(node, problem) < heuristic(startNode, problem):
                    startNode = node
                    break
                succStates = problem.getSuccessors(node)
                for succState in succStates:
                    succNode, succAction, succCost = succState
                    newState = (succNode, succAction, cost + succCost, path + [(node, action)])
                    myqueue.push(newState)
    path = path + [(node, action)]
    actions = [action[1] for action in path]
    del actions[0]
    return actions


def idaStarSearch(problem, heuristic=nullHeuristic):
    root = problem.getStartState()
    bound = heuristic(problem.getStartState(), problem)
    action = ''
    path = [(root, action)]
    loop = True
    global result

    while loop:
        t = search(path, 0, bound, problem, heuristic)
        if t == "Found":
            loop = False
        elif t == float('inf'):
            loop = False
        else:
            bound = t
    path = result
    result = []
    actions = [action[1] for action in path]
    del actions[0]
    return actions


def search(path, cost, bound, problem, heuristic):
    global result
    result = []
    reversedPath = path[::-1]
    node = reversedPath[0][0]
    f_value = cost + heuristic(node, problem)
    if f_value > bound:
        return f_value
    if problem.isGoalState(node):
        result = path
        return "Found"

    min_t = float('inf')
    succLists = problem.getSuccessors(node)
    for succState in succLists:
        succNode, succAction, succCost = succState
        if [(succNode, succAction)] not in path:
            path = path + [(succNode, succAction)]
            t = search(path, cost + succCost, bound, problem, heuristic)
            if t == "Found":
                return "Found"
            if t < min_t:
                min_t = t
            path.remove((succNode, succAction))
    return min_t


                
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ehc = enforcedHillClimbing
ida = idaStarSearch