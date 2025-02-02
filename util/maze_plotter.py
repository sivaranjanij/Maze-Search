import matplotlib.pyplot as plt

def maze_plotter(maze, search_algorithm, path_length=0):
    """
    Plots the final state of the maze and saves the plot as an image file.

    Parameters:
        maze (2D array-like): The maze to be plotted, where each element represents a cell in the maze.
        search_algorithm (str): A string indicating the type of search algorithm used. 

    Returns:
        None
    """

    # Create a new figure and axis for the plot
    fig, ax = plt.subplots()

    # Clear the current axis
    ax.cla()

    # Get the default colormap and set the color for bad values (e.g., masked cells) to white
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")

    ax.set_title(search_algorithm.upper()+" - Path Length : "+str(path_length), fontsize=16, color='red', loc='center')

    # Set the x-axis limits with some padding
    plt.xlim(-10,len(maze)+10)
    # Set the y-axis limits with some padding and invert the y-axis
    plt.ylim(len(maze)+10,-10)

    # Display the maze using the colormap and draw the plot
    ax.imshow(maze, cmap=cmap)
    plt.draw()


    # Save the plot as an image file based on the provided filename
    plt.savefig(f'figures/{search_algorithm}-maze.png', dpi=1000, bbox_inches='tight')
    plt.show()