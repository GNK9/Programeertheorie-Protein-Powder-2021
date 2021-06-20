import numpy as np 
from visualisation.visualisation import display_protein

import numpy as np 

class Bfs():
    def __init__(self, chain, start_pos = [[(0,0),(0,1)]], next_best = [], stability=0):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = start_pos
        self.tuple_length = len(self.start_pos[0])
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
        self.next_best = next_best
        self.stability = stability
    
    def get_permutations(self, loops):
        start = self.start_pos
        if loops - len(self.start_pos[0]) > 0:
            for x in range(loops - len(self.start_pos[0])):
                self.tuple_length += 1
                combinations = [[*positions,tuple(np.add(positions[-1],direction))] 
                                for positions in start
                                for direction in self.directions
                                if len(set([*positions,tuple(np.add(positions[-1],direction))])) == self.tuple_length]
                start = combinations
            if not combinations:
                return False
            return combinations
        return start
        
    def score_protein(self, protein):
        stability = 0
        for x in range(self.chain_length):
            for y in range(x+2, self.chain_length):
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
        best = {self.score_protein(permutation): permutation for permutation in permutations}
        if len(best.keys()) == 1:
            return min(best.items())[0], permutations, []
        return min(best.items())[0],[min(best.items())[1]],best 
        
chain = "HPPPPPPPPPPPPHPPPPPPPPPHPPPPPPPHPPPPPPPPH"
sequence = ''
new_start = [[(0,0),(0,1)]]
next_best = []

for amino in chain:
    sequence += amino
    length_seq = len(sequence)
    if amino in {"C","H"}:
        test = Bfs(sequence, start_pos = new_start, next_best= next_best)
        permutations = test.get_permutations(length_seq)
        if not permutations:
            del next_best[min(next_best)]
            for stability,coord in sorted(next_best.items(), key=lambda x: x[1], reverse=True):
                permutations = Bfs(sequence, start_pos = [coord], next_best= next_best).get_permutations(length_seq)
                if permutations:
                    break
                    
        stability, new_start, next_best = test.get_best_permutation(permutations)
        
display_protein(new_start[0], chain, stability)