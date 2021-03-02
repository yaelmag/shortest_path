from ways import info


class MapProblem:

    def __init__(self, s_start, goal, graph):
        self.s_start = graph.get_junction(s_start)
        self.goal = graph.get_junction(goal)
        self.graph = graph

    def actions(self, s):
        return s.links

    def succ(self, s, a):
        if a in s.links:
            return self.graph.get_junction(a.target)
        raise ValueError(f'No route from {s} through {a}')

    def is_goal(self, s):
        return s == self.goal

    def step_cost(self, a):
        dis = a.distance
        speed = info.SPEED_RANGES[a.highway_type-1][1]
        return dis / speed

    def state_str(self, s):
        return s

    def __repr__(self):
        return {'s_start': self.s_start, 'goal': self.goal}