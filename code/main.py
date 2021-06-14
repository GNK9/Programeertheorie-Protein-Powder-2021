from classes.protein import Protein
from algorithms.bfs import Bfs  
from visualisation.visualisation import display_protein

chain = "HHPHHHPHPHHHPH"
permutations = Bfs(chain)
evaluate = Protein(chain)

display_protein(evaluate.get_best_permutation(permutations.get_permutations())[1],chain)