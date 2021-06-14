from classes.protein import Protein
from algorithms.bfs import Bfs  
from visualisation.visualisation import display_protein
import random
import timeit

# Initialization
chain = "HHPHHHPHPHHHPH"
chain2 = "HPHPPHHPHPPHPHHPPHPH"
permutations = Bfs(chain)
evaluate = Protein(chain)

# Baseline 
start = timeit.default_timer()
baseline = Bfs(chain2)
print(f'Solution: {random.choice(baseline.get_permutations())}')
stop = timeit.default_timer()
print(f'Baseline Duration: {stop-start:.4f} seconds.')

# Algorithm 1- visualisation
# display_protein(evaluate.get_best_permutation(permutations.get_permutations())[1],chain)