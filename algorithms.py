import MapProblem
from ways import graph, tools
from Node import Node
from PriorityQueue import PriorityQueue
import math

def find_ucs_route(start, goal):
    g = graph.load_map_from_csv()
    problem = MapProblem.MapProblem(start, goal, g)
    return uniform_cost_search(problem)


def find_astar_route(start, goal):
    g = graph.load_map_from_csv()
    problem = MapProblem.MapProblem(start, goal, g)
    return astar_search(problem)


def find_idastar_route(start, goal):
    g = graph.load_map_from_csv()
    problem = MapProblem.MapProblem(start, goal, g)
    def g(node):
        return node.path_cost
    def h(node):
        distance = tools.compute_distance(node.state.lat, node.state.lon, problem.goal.lat, problem.goal.lon)
        # 110 max speed, 1000 to convert to meters
        return distance / (110*1000)
    return idastar_search(problem, f=lambda n: g(n)+h(n))


def best_first_graph_search(problem, f):
    node = Node(problem.s_start)
    frontier = PriorityQueue(f) #Priority Queue
    frontier.append(node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node.solution()
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None


# f = g:
def uniform_cost_search(problem):
    def g(node):
        return node.path_cost
    return best_first_graph_search(problem, f=g)


def astar_search(problem):
  def g(node):
    return node.path_cost
  def h(node):
      distance = tools.compute_distance(node.state.lat, node.state.lon, problem.goal.lat, problem.goal.lon)
      # 110 max speed, 1000 to convert to meters
      return distance / (110 * 1000)
  return best_first_graph_search(problem, f=lambda n: g(n)+h(n))


def dfs_contour(node, f_limit, next_f, f, problem):
    if f(node) > f_limit:
        return None, min(f(node), next_f)
    if problem.is_goal(node.state):
        return node.solution(), f_limit
    if (node is None):
        pass
    for n in node.expand(problem):
        solution, new_f = dfs_contour(n, f_limit, next_f, f, problem)
        if solution is not None:
            return solution, f_limit
        next_f = min(next_f, new_f)
    return None, next_f


def idastar_search(problem, f):
    root = Node(problem.s_start)
    f_limit = f(root)
    next_f = math.inf
    while(True):
        solution, f_limit = dfs_contour(root, f_limit, next_f, f, problem)
        print(f_limit)
        if solution is not None:
            return solution
        if f_limit == math.inf:
            return None
