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
        
        [stability := stability-1 for x in range(len(H_coords)) for y in range(1,len(H_coords))
        if sum(map(abs,np.subtract(H_coords[x],H_coords[y]))) == 1]

        return stability

    # Calculates score with Cystein in chain.
    def score_protein_cyst(self, protein):
        stability = 0
        H_coords = [protein[amino] for amino in range(len(self.chain)) if self.chain[amino] == 'H' if self.chain[amino] == 'C']
        C_coords = [protein[amino] for amino in range(len(self.chain)) if self.chain[amino] == 'C']

        [stability := stability-1 for x in range(len(H_coords)) for y in range(1,len(H_coords))
        if sum(map(abs,np.subtract(H_coords[x],H_coords[y]))) == 1]
        [stability := stability-5 for x in range(len(C_coords)) for y in range(1,len(C_coords))
        if sum(map(abs,np.subtract(C_coords[x],C_coords[y]))) == 1]

        return stability

    def get_best_permutation(self, permutations):
        return min({self.score_protein(permutation): permutation for permutation in permutations}.items())

    # Gets best permutaiton with Cystein in chain.
    def get_best_permutation_cyst(self, permutations):
        return min({self.score_protein_cyst(permutation): permutation for permutation in permutations}.items())