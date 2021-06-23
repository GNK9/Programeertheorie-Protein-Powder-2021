from classes.protein import Protein
from algorithms.bfs import Bfs  
from visualisation.visualisation import display_protein
from algorithms.baseline import baseline
from algorithms.bfs_greedy import Bfs_greedy
from output.output import output
import timeit

def main(chain, greedy = True):
    # Initialization.
    evaluate = Protein(chain)
    
    # Generate Bfs-permutations & measure duration.
<<<<<<< HEAD
    # bfs_start = timeit.default_timer()
    # permutations = Bfs(chain).get_permutations()
    # bfs_stop = timeit.default_timer()
    # bfs_time = bfs_stop-bfs_start

    #Baseline
    # baseline(permutations, bfs_time)
=======
    #bfs_start = timeit.default_timer()
    #permutations = Bfs(chain).get_permutations()
    #bfs_stop = timeit.default_timer()
    #bfs_time = bfs_stop-bfs_start

    #Baseline
    #baseline(permutations, bfs_time)
>>>>>>> ed5eb90abd6499842194501dd9d791abf46d65da

    #-------------------------------------- Bfs-Greedy-algorithm --------------------------------------------------#
    if greedy:
        start = timeit.default_timer()
        stability,result = Bfs_greedy(chain).stable_permutation()
        print(stability,result)
        stop = timeit.default_timer()
        return print(f'Bfs-greedy Duration: {stop-start:.4f} seconds.'), display_protein(result[0], chain, stability), output(chain, result[0], stability)

    #-------------------------------------- Bfs-algorithm ---------------------------------------------------------#

    # Measure Stability & duration.
    start = timeit.default_timer()
    stability,result = evaluate.get_best_permutation(permutations)
    stop = timeit.default_timer()
    return print(f'Bfs Duration: {stop-start+bfs_time:.4f} seconds.'), display_protein(result[0], chain, stability)


if __name__ == "__main__":
<<<<<<< HEAD
    main("HHPHHHPHPHHHPH", greedy=True)
=======
    main("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", greedy=True)
>>>>>>> ed5eb90abd6499842194501dd9d791abf46d65da
