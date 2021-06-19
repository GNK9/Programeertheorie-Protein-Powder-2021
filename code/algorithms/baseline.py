import random
import timeit

def baseline(permutations, bfs_time): 
    start = timeit.default_timer()
    print(f'Baseline Solution: {random.choice(permutations)}')
    stop = timeit.default_timer()
    return print(f'Baseline Duration: {stop-start+bfs_time:.4f} seconds.')