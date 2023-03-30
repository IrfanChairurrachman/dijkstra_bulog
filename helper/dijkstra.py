from scipy.sparse.csgraph import shortest_path
import pandas as pd

class Dijkstra:
    """
    A class to represent Djikstra object

    Djikstra method calculated by scipy library
    """
    def __init__(self, M, idx):
        self.M = M
        self.idx = idx
        self.D, self.Pr = shortest_path(M, directed=False, method='D', return_predecessors=True)
    
    def path(self, start = 0, last = 1):
        return Path(self.M, self.idx, start, last)

class Path(Djikstra):
    """
    A class to represent Path of Djikstra object
    """
    def __init__(self, M, idx, start, last):
        super().__init__(M, idx)
        self.start = start
        self.last = last
        self.path = self.get_path_idx()
    
    def get_path_idx(self):
        start, last = self.start, self.last
        path = [last]
        dist = 0
        k = last
        while self.Pr[start, k] != -9999:
            path.append(self.Pr[start, k])
            dist += self.D[k, path[-1]]
            k = self.Pr[start, k]
        
        return path[::-1]
    
    def get_cost(self):
        path = self.path
        dist = 0
        for i in range(len(path)-1):
            pre, suc = path[i], path[i+1]
            dist += self.D[pre, suc]
        return dist
    
    def get_path_name(self):
        return self.idx[self.path].tolist()