import csv
from matplotlib.pyplot import xkcd
import numpy as np

def output(chain, permutation, stability):
    """
    Output protein configuration to csv
    input: [{Amino-acid: position}...]
    output: CSV
    """
    with open('C:/Users/Ali/Desktop/Programeertheorie-Protein-Powder-2021/code/output/output.csv', newline="", mode='w') as output_file:
        directions = {(1,0):1, (0,1):2, (-1, 0):-1, (0,-1):-2}
        headers = ['amino','fold']
        writer = csv.writer(output_file)
        writer.writerow(headers)
        output = [(chain[x],directions[tuple(np.subtract(permutation[x],permutation[x - 1]))]) if x > 0 else (chain[x], 0) 
                for x in range(0, len(permutation))]
        [writer.writerow(result) for result in output[::-1]]
        writer.writerow(('score',stability))
        return