import matplotlib.pyplot as plt

"""
Plots the final state of the maze and saves the plot as an image file.

Parameters:
maze (2D array-like): The maze to be plotted, where each element represents a cell in the maze.
s (str): A string indicating the type of search algorithm used. 
         If 'a', the plot will be saved as 'a_star-new.png'.
         Otherwise, the plot will be saved as 'bfs-new.png'.

Returns:
None
"""
def maze_plot_final(maze, search_algorithm):
    # Create a new figure and axis for the plot
    fig, ax = plt.subplots()

    # Clear the current axis
    ax.cla()

    # Get the default colormap and set the color for bad values (e.g., masked cells) to white
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")

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