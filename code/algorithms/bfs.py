import numpy as np

class Bfs():
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = [(0,0),(0,1)]
        self.tuple_length = 2
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def get_permutations(self):
        start = [self.start_pos]
        loops = self.chain_length-2
        
        if loops:
            for x in range(loops):
                self.tuple_length += 1
                combinations = [[*positions,tuple(np.add(positions[-1],direction))] 
                                for positions in start
                                for direction in self.directions
                                if len(set([*positions,tuple(np.add(positions[-1],direction))])) == self.tuple_length]
                start = combinations
            return combinations
        return start