from util.maze_plotter import maze_plotter
from util.traversable_neighbors import traversable_neighbors


def dfs_path_printer(dfs_maze, dfs_path):
    """
    Marks the path from the source node to the destination node in a DFS (Depth-First Search) explored maze.

    Parameters:
    dfs_maze : list of lists (2D matrix)
        An nxn matrix representing the maze, where different values indicate walls, open paths, or visited cells.

    dfs_path : list of tuples
        A list of coordinates (row, col) representing the path taken by DFS.

    Functionality:
    - Marks the start and destination nodes distinctly.
    - Marks the path taken by DFS in the maze.

    Returns:
    None
    """

    for node in dfs_path:
        # Mark the current node as part of the path
        dfs_maze[node] = -2

    # Mark the destination node with a special identifier (-2) to highlight it in the visualization.
    dfs_maze[len(dfs_maze) - 1][len(dfs_maze) - 1] = -2

    # Mark the source node with the same identifier to differentiate it in the visualization.
    dfs_maze[0][0] = -2

    maze_plotter(dfs_maze, "dfs", len(dfs_path))
    return


def depth_first_search(dfs_maze, display=True):
    """
    Implements the Depth First Search (DFS) approach to solve a given maze.

    Parameters:
    dfs_maze : list of lists (2D matrix)
        An nxn matrix representing the randomly generated maze, where open paths are represented by 0
        and walls are represented by 1.

    display : bool, optional (default=True)
        A control parameter to display the output maze plot with the path, if True. If False, no plot will be displayed.
    
    Returns:
    int : 1 if a path from source to destination is found, 0 otherwise.
    """

    # Create a copy of the maze to avoid modifying the original input
    dfs_maze = dfs_maze.copy()

    # Define the source (starting point) and destination (goal).
    source, destination = (0, 0), (len(dfs_maze) - 1, len(dfs_maze) - 1)

    # Mark the source node with the same identifier to differentiate it in the visualization.
    dfs_maze[source] = -1

    # Initialize the DFS stack with the source node
    dfs_stack = [source]

    # Initialize an empty list to store the path taken by DFS
    dfs_path = []

    # Flag variable to track if the path is found (0 = not found, 1 = found)
    pathFound = 0

    """
    Continue searching until:
    1. The DFS stack is empty, meaning all possible nodes have been explored and no path to the destination is found.
    2. The pathFound flag is set to True, meaning a path has been found from the source to the destination.
    """
    while len(dfs_stack) != 0 and pathFound == 0:
        # Pop the last visited node from the DFS stack (LIFO order)
        cur_node = dfs_stack.pop()

        # Append the current node to the path list
        dfs_path.append(cur_node)

        # Mark the current node as visited by setting its value to -2 (different from visited cells)
        dfs_maze[cur_node] = -2

        # Get all the traversable neighbors of the current node
        neighbors = traversable_neighbors(dfs_maze, cur_node)

        # If no neighbors are found, it indicates a dead-end, so pop the node from the path
        if len(neighbors) == 0:
            dfs_path.pop()
        else:
            # Iterate over all neighbors
            for node in neighbors:
                # Check if any neighbor is the destination node
                if node == destination:
                    #If the nrighbor is the destination the set pathFound to True and
                    #return the path.
                    dfs_maze[destination] = -2

                    # Set pathFound to 1 to signify that a path was found
                    pathFound = 1
                    if display:
                        #If the display parameter is set to true the plot the path
                        dfs_path_printer(dfs_maze, dfs_path)
                    return 1
                
                # Append the neighbor node to the DFS stack for further exploration
                dfs_stack.append(node)

        # Mark the current node as visited by setting its value to -1
        # This prevents revisiting the node in the future
        dfs_maze[cur_node] = -1

    # If the DFS stack is empty and no path was found, return 0
    if pathFound == 0:
        if display:
            # If display is True, plot the maze showing all visited nodes
            print("No path found :(")
            maze_plotter(dfs_maze, "dfs")
        
        # Return 0 indicating that no path was found
        return 0