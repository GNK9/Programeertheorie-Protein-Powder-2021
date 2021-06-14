from classes.protein import Protein
from algorithms.bfs import Bfs  
from visualisation.visualisation import display_protein
import random
import timeit

# Initialization
chain = "HHPHHHPHPHHHPH"
chain2 = "HPHPPHHPHPPHPHHPPHPH"
chain3 = "CPPC"
permutations = Bfs(chain3)
evaluate = Protein(chain3)

# Baseline 
start = timeit.default_timer()
baseline = Bfs(chain3)
print(f'Solution: {random.choice(baseline.get_permutations())}')
stop = timeit.default_timer()
print(f'Baseline Duration: {stop-start:.4f} seconds.')

# Algorithm 1- visualisation
print(evaluate.get_best_permutation(permutations.get_permutations()),chain3)

# Algorithm 1- visualisation (with Cysteine)
print(evaluate.get_best_permutation_cyst(permutations.get_permutations()),chain3)