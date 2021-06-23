import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def display_protein(coordinates, chain, stability):

    fig, ax = plt.subplots()
    Path = mpath.Path

    # path all coordinates
    path_data = [x for x in coordinates]
    verts = path_data
    path = mpath.Path(verts)
    
    # plot control points and connect lines of all coordinates
    x, y = zip(path.vertices)
    line, = ax.plot(x, y, color='black', marker='o',
     markerfacecolor='blue', linewidth = 3, markeredgecolor='blue', markersize=16)

    # path only the "H" protein coordinates
    path_data = [x[0] for x in zip(coordinates, chain) if x[1] == "H"]
    verts = path_data
    path = mpath.Path(verts)

    # plot control points and connect lines of "H" protein coordinates
    x, y = zip(path.vertices)
    line, = ax.plot(x, y, color='red', linestyle = 'None', marker='o',
     markerfacecolor='red', markeredgecolor='red', markersize=16)

    # only if there are "C" proteins in the chain, path the coordinates
    if "C" in chain: 
        path_data = [x[0] for x in zip(coordinates, chain) if x[1] == "C"]
        verts = path_data
        path = mpath.Path(verts)

        # plot control points and connecting lines
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, color='green', linestyle = 'None', marker='o',
        markerfacecolor='green', markeredgecolor='green', markersize=16)

    # legend
    fpoints = mpatches.Patch(color='blue', label='"P" protein')
    hpoints = mpatches.Patch(color='red', label='"H" protein')
    cpoints = mpatches.Patch(color='green', label='"C" protein')

    # plot the graph
    ax.grid()
    ax.axis('equal')
    plt.legend(handles=[fpoints, hpoints, cpoints])
    plt.suptitle( f"Stability Score: {stability}")
    plt.title( f"Chain: {chain}")
    plt.show()