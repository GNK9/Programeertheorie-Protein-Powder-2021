import numpy as np

class Bfs():
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = (0,0)
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def get_permutations(self):
        start = [[self.start_pos]]
        tuple_length = 1
        
        for x in range(self.chain_length-1):
            tuple_length += 1
            combinations = [ [*positions,tuple(np.add(positions[-1],direction))] for positions in start
                           for direction in self.directions
                           if len(set([*positions,tuple(np.add(positions[-1],direction))])) == tuple_length  ]
            start = combinations
        return combinations[:int(len(combinations)/2)]