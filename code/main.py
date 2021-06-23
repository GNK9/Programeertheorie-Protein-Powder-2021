from algorithms.bfs import Bfs  
from visualisation.visualisation import display_protein
from algorithms.baseline import baseline
from algorithms.bfs_greedy import Bfs_greedy
from output.output import output
import timeit

def main(chain, greedy = True):
    #-------------------------------------- Bfs-Greedy-algorithm --------------------------------------------------#
    if greedy:
        start = timeit.default_timer()
        stability,result = Bfs_greedy(chain).stable_permutation()
        stop = timeit.default_timer()
        return print(f'Bfs-greedy Duration: {stop-start:.4f} seconds.'), display_protein(result[0], chain, stability), output(chain, result[0], stability)

    #-------------------------------------- Bfs-algorithm ---------------------------------------------------------#

    # Measure stability & duration of bfs-algorithm.
    start = timeit.default_timer()
    bfs = Bfs(chain)
    permutations = bfs.get_permutations()
    stability,result = bfs.get_best_permutation(permutations)
    stop = timeit.default_timer()

    # Measures baseline duration.
    baseline(permutations)
    
    return print(f'Bfs Duration: {stop-start:.4f} seconds.'), display_protein(result, chain, stability), output(chain, result, stability)


if __name__ == "__main__":
    main("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", greedy=True)
