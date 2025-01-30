
def traversable_neighbors(maze, node):
    """
    Given a maze and a node, this function returns a list of traversable neighbors.

    Args:
        maze (list of list of int): A 2D list representing the maze where 1 represents a wall, 
                                    -1 represents a visited cell, and any other value represents 
                                    an unvisited traversable cell.
        node (tuple of int): A tuple (row, coloumn) representing the current node's position in the maze.

    Returns:
        list of tuple of int: A list of tuples representing the positions of traversable neighbors 
                              of the given node. A neighbor is considered traversable if it is 
                              within the maze boundaries, not a wall, and not already visited.
    """

    #Sets the current node and initializes an empty neighbors array
    (i,j) = node
    neighbors = []

    #The offsets for the four possible neighbors of a cell
    neighbor_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for offset in neighbor_offsets:
        x, y = i + offset[0], j + offset[1]

        #Checks if the cell is within the maze boundaries and is not a wall(1) or already visited(-1)
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1 and maze[x][y] != -1:
            neighbors.append((x, y))

    #Returns the list containing the traversable neighbors
    return neighbors