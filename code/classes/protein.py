import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

class Protein():
    def __init__(self, chain):
        self.chain = list(chain)
        self.chain_length = len(self.chain)
        self.start_pos = [0,0]

    def get_permutations(self):
        start = [[self.start_pos]]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for x in range(self.chain_length-1):
            combinations = [[*positions, list(np.add(direction,positions[-1]))] 
                            for positions in start for direction in directions 
                            if list(np.add(direction,positions[-1])) not in positions]
            start = combinations
        return combinations

#Tijdelijk
def display_protein(coordinates):

    fig, ax = plt.subplots()

    Path = mpath.Path
    path_data = [x for x in coordinates]
    verts = path_data
    path = mpath.Path(verts)

    # plot control points and connecting lines
    x, y = zip(*path.vertices)
    line, = ax.plot(x, y, 'co-', markersize=14)
    
    #Add Annotations
    for i,j in zip(x,y):
        corr = -0.02
        ax.annotate('H',  xy=(i + corr, j + corr))

    ax.grid()
    ax.axis('equal')
    plt.show()

# TEST CODE
test = Protein("HPPPHHPHPH")
all = [display_protein(x) for x in test.get_permutations()[10000:]]
