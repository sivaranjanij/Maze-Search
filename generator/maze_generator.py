import random
import numpy as np

"""
Generates a square maze of given dimension with walls placed based on the given probability.

Parameters:
dimension (int): The size of the maze (dimension x dimension).
probabillity (float): The probability of placing a wall in each cell (0 <= probability <= 1).

Returns:
numpy.ndarray: A 2D numpy array representing the generated maze, where 0 represents an empty cell and 1 represents a wall.
"""
def maze_generator(dimension, probabillity):

    # Initialize the maze with all empty cells
    maze = np.zeros((dimension, dimension), dtype = int)

    # Loop through each cell in the maze, and set it to a wall with probabillity value.
    for i in range(dimension):
        for j in range(dimension):
            if random.random() <= probabillity:
                maze[i][j] = 1

    # Once the maze is generated, set the start and end points to 0    
    maze[0][0] = 0
    maze[dimension - 1][dimension - 1] = 0
    return maze