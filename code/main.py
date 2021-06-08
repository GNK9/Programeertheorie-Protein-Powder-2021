from classes.protein import Protein
from visualisation.visualisation import display_protein

chain = "HHPHHHPHPHHHPH"
test = Protein(chain)

print(display_protein(test.get_best_permutation(test.get_permutations())[1],chain))
