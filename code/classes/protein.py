import numpy as np

class Protein():
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = [0,0]
        self.directions = [[0,1], [1,0], [0,-1], [-1,0]]

    def score_protein(self, protein):
        stability = 0
        H_coords = [protein[amino] for amino in range(len(self.chain)) if self.chain[amino] == 'H']
        
        [ stability := stability-1 for x in range(len(H_coords)) for y in range(1,len(H_coords))
        if sum(map(abs,np.subtract(H_coords[x],H_coords[y]))) == 1]

        return stability

    def get_best_permutation(self, permutations):
        return min({self.score_protein(permutation): permutation for permutation in permutations}.items())