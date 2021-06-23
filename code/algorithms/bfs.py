import numpy as np

class Bfs():
    """ 
    Generates all permutations in state space. 
    Due to the nature of the Breadth-first search
    and the size of the state space, it will lead to 
    a memory error on some chain-lengths.  
    """
    # Configure starting point and directions in grid.
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = [(0,0),(0,1)]
        self.tuple_length = 2
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    # Function to generate all permutations.   
    def get_permutations(self):
        start = [self.start_pos]
        loops = self.chain_length-2
        
        # Loop over each direction and save the configuration
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

    def score_protein(self, protein):
        stability = 0
        chain_length = len(protein)
        for x in range(chain_length):
            for y in range(x+2, chain_length):
                # Checks for Cystein-bonds.
                if self.chain[x] == 'C' and self.chain[y] == "C":
                    if sum(map(abs,np.subtract(protein[x],protein[y]))) == 1:
                        stability -= 5 
                
                # Checks for H-bonds.
                elif self.chain[x] in {'H','C'} and self.chain[y] in {'H','C'}:
                    if sum(map(abs,np.subtract(protein[x],protein[y]))) == 1:
                        stability -= 1 
        return stability

    def get_best_permutation(self, permutations):
        return min({self.score_protein(permutation): permutation for permutation in permutations}.items())