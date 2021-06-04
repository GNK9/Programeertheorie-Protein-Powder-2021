import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

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
display_protein([(0,0), (0,1), (1,1)])