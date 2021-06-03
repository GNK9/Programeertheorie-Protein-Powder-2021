class Stability():
    def __init__(self, permutations):
        self.permutations = permutations
        self.stable_permutation = ''

    def stable_configurations(self):
        self.stable_permutation = self.permutations[0]
        return self.stable_permutation

    def score(self):
        return self.stable_permutation.append(('score', '-2'))