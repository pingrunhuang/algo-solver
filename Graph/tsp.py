"""
given a fully connected undirected graph(If no path exists between two cities, adding an arbitrarily long edge will complete the graph without affecting the optimal tour),
find the path with the lowest cost in total for a salesman to travel from a given start vertex
"""
import time

class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight
    
    def __repr__(self):
        return self.target
    


class TSP(object):
    """
    This is a fully connected graph with edge weight value positive
    """
    def __init__(self):
        self.graph = {}
        self.prev = {}
        self.start = None

    def add_vertex(self, name, edges):
        self.graph[name] = edges

    def permutation(self, edge, result=[]):
        if edge.target == self.start:
            return result
        
        for x in result:
            if x.target == edge.target:
                return result
        result.append(edge)

        for next_edge in self.graph[edge.target]:
            self.permutation(next_edge, result)
        return result

    def tsp_recursive(self, start):
        """
        Essentially, the tsp problem is a permutation problem
        """
        self.start = start
        result = []
        for edge in self.graph[start]:
            result.append(self.permutation(edge, [Edge(start, 0)]))
        smallest_val = 100000
        print(result)
        path = []
        for solution in result:
            total_cost = sum(map(lambda x:x.weight, solution))
            if smallest_val>total_cost:
                path = solution
                smallest_val = total_cost
        return (smallest_val, path)

    def tsp_dp(self, graph, start):
        pass


if __name__ == "__main__":
    tsp = TSP()
    tsp.add_vertex('w', [Edge('y', 1), Edge('x', 6), Edge('z', 3)])
    tsp.add_vertex('x', [Edge('w', 6), Edge('z', 3), Edge('y', 4)])
    tsp.add_vertex('z', [Edge('y', 2), Edge('w', 3), Edge('x', 3)])
    tsp.add_vertex('y', [Edge('w', 1), Edge('x', 3), Edge('z', 2)])
    result = tsp.tsp_recursive('x')
    print(result)