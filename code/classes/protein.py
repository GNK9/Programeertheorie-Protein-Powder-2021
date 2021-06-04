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
test = Protein("HPP")
test.construct_permutations()

# Protein, Chain, Stability, constructor, display protein

# coordinates = [[0, 0]]
# currentcoord = [0, 0]
# for protein in beststring:
#   if protein.value = 1: rechts
#       currentcoord[0] = currentcoord[0] + 1
#       coordinates.append(currentcoord)

#   if protein.value = -1: links
#       currentcoord[0] = currentcoord[0] - 1
#       coordinates.append(currentcoord)

#   if protein.value = 2: boven
#       currentcoord[0] = currentcoord[0] + 2
#       coordinates.append(currentcoord)

#   if protein.value = -2: onder
#       currentcoord[0] = currentcoord[0] - 2
#       coordinates.append(currentcoord)
