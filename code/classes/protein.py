import itertools 

class Protein():
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)

    def construct_permutations(self):
        combinations = itertools.product(['-1', '-2', '1', '2'], repeat=self.chain_length-1)
        combinations = [ ('0', ) + x for x in combinations]
        combinations = [ list(zip(self.chain, x)) for x in combinations]

        return print(list(combinations))

# TEST CODE
test = Protein("HHPHHHPPPPPH")
test.construct_permutations()
    
# Protein, Chain, Stability, constructor, display protein