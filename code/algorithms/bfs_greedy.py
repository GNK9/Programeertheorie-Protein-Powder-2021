import numpy as np

class Bfs_greedy():
    def __init__(self, chain):
        self.chain = chain
        self.chain_length = len(chain)
        self.sequence = ''
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
        self.start_coords = [[(0,0),(0,1)]]
        
    def stable_permutation(self):
        permutations = self.start_coords
        for amino in self.chain:
            self.sequence += amino
            if amino in {"H","C"} and len(self.sequence) > 2:
                permutations = self.generate_permutations(permutations)
                if not permutations:
                    del scored_permutations[stability]
                    for stability,permutation in sorted(scored_permutations.items(), key=lambda x: x[1], reverse=True):
                        permutations = self.generate_permutations([permutation])
                        if permutations:
                            break
                scored_permutations = {self.score_protein(permutation):permutation for permutation in permutations}
                if len(scored_permutations) > 1:
                    stability = min(scored_permutations.items())[0]
                    permutations = [min(scored_permutations.items())[1]]
        return stability,permutations
                
    def generate_permutations(self, permutations):
        sequence_length = len(permutations[0])
        for x in range(len(self.sequence) - sequence_length):
            sequence_length += 1 
            new_permutations = [[*coords,tuple(np.add(coords[-1],direction))]
                                for coords in permutations
                                for direction in self.directions
                                if len(set([*coords,tuple(np.add(coords[-1],direction))])) == sequence_length]
            permutations = new_permutations
        return new_permutations

    def score_protein(self, protein):
        stability = 0
        for x in range(len(protein)):
            for y in range(x+2, len(protein)):
                # Checks for Cystein-bonds.
                if self.chain[x] == 'C' and self.chain[y] == "C":
                    if sum(map(abs,np.subtract(protein[x],protein[y]))) == 1:
                        stability -= 5 
                
                # Checks for H-bonds.
                elif self.chain[x] in {'H','C'} and self.chain[y] in {'H','C'}:
                    if sum(map(abs,np.subtract(protein[x],protein[y]))) == 1:
                        stability -= 1 
        return stability