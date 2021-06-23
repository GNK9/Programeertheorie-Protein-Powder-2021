import random
import timeit

# function to calculate the baseline with elapsed time.
def baseline(permutations): 
    start = timeit.default_timer()
    print(f'Baseline Solution: {random.choice(permutations)}')
    stop = timeit.default_timer()
    return print(f'Baseline Duration: {stop-start:.4f} seconds.')