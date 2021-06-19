import numpy as np

class Protein():
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = [0,0]
        self.directions = [[0,1], [1,0], [0,-1], [-1,0]]

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
        return min({self.score_protein(permutation): permutation for permutation in permutations}.items())