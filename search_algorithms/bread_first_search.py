import matplotlib.pyplot as plt
from util.maze_plotter import maze_plotter
from util.traversable_neighbors import traversable_neighbors
import numpy as np
from collections import deque

def bfs_path(bfs_maze, cur_node, bfs_parent):
    """
    Traces back and marks the shortest path from the destination node to the source node 
    in a BFS (Breadth-First Search) explored maze and visualizes the result.

    Parameters:
    bfs_maze (ndarray): An n x n matrix representing the maze, where different values 
                        indicate walls, open paths, or visited cells.
    cur_node (tuple): The coordinates (row, col) of the last node reached before 
                      finding the destination.
    bfs_parent (list of list of tuples): A matrix of the same dimensions as bfs_maze 
                                         that stores the parent (previous node) 
                                         of each cell in the shortest path.

    Functionality:
    - Marks the start and destination nodes distinctly.
    - Traces back from the destination to the source using bfs_parent.
    - Counts and prints the path length.
    - Visualizes the marked path.

    Returns:
    None
    """

    # Mark the destination node with a special identifier (-2) to highlight it in the visualization.
    bfs_maze[len(bfs_maze)-1, len(bfs_maze)-1] = -2

    # Mark the source node with the same identifier to differentiate it in the visualization.
    bfs_maze[0,0] = -2

    # Initialize path length count (including the source and destination).
    count = 2
    temp_node = cur_node # Start backtracking from the destination node.

    # Trace the path backward from the destination node to the source node.
    while temp_node != (0,0):

        # Mark the current node as part of the shortest path.
        bfs_maze[temp_node] = -2
        (i,j) = temp_node

        # Move to the parent node of the current node.
        temp_node = bfs_parent[i][j]

        # Increment path length count.
        count += 1

    # Output the total number of nodes in the shortest path.
    print("Path length : ",count)

    # Visualize the marked path using maze_plotter.
    maze_plotter(bfs_maze,"bfs")
    return


def breadth_first_search(bfs_maze,display=True):
    """
    Performs Breadth-First Search (BFS) to find the shortest path from the source 
    (top-left) to the destination (bottom-right) in a given maze.

    Parameters:
    bfs_maze (ndarray): An n x n matrix representing the maze, where different values 
                        indicate walls, open paths, or visited cells.
    display (bool): If True, visualizes the search process and the path (default: True).

    Functionality:
    - Implements BFS using a queue to explore the shortest path.
    - Tracks visited nodes and stores parent-child relationships to reconstruct the path.
    - If a path is found, it optionally visualizes the result.
    - If no path is found, it displays the explored maze.

    Returns:
    int: 1 if a path is found, 0 if no path exists.
    """

    # Define the source (starting point) and destination (goal).
    source, destination = (0,0), (len(bfs_maze)-1, len(bfs_maze)-1)

    # Create a copy of the maze to avoid modifying the original.
    bfs_maze=bfs_maze.copy()

    # Initialize the BFS queue with the source node.
    bfs_queue = deque([source])

    # Mark the source node as visited (-1).
    bfs_maze[source] = -1

    # Flag to track if a path to destination is found.
    pathFound = 0

    # Matrix to store parent nodes for reconstructing the path.
    bfs_parent = [[None for _ in range(len(bfs_maze))] for _ in range(len(bfs_maze))]

    """
    Continue BFS until:
    1. The queue becomes empty, meaning all possible nodes have been explored 
       without reaching the destination.
    2. A path to the destination is found, breaking the loop early.
    """
    while len(bfs_queue) != 0 and pathFound == 0:

        # Dequeue the first node in FIFO order (BFS characteristic).
        cur_node = bfs_queue.popleft()
        bfs_maze[cur_node] = -2 # Temporarily mark as processing.

        # Get all valid neighbors that can be traversed.
        neighbors = traversable_neighbors(bfs_maze, cur_node)

        # Iterate through the neighbors to continue the BFS.
        if len(neighbors) != 0:
            for node in neighbors:
                (i,j) = node
                if node == destination:
                    # If the destination is found, set the flag and exit.
                    pathFound = 1
                    if display:
                        # If visualization is enabled, plot the discovered path.
                        bfs_path(bfs_maze, cur_node, bfs_parent)
                        break
                    return 1
                
                 # If the neighbor hasn't been visited, mark its parent and add to queue.
                if bfs_parent[i][j] == None:
                    bfs_parent[i][j] = cur_node
                    bfs_queue.append(node)

        # Mark the current node as visited (-1).
        bfs_maze[cur_node] = -1

    # If the loop completes without finding a path, return failure.
    if pathFound == 0:
        if display:
            # If visualization is enabled, display the explored maze.
            print("No Path Found :(")
            maze_plotter(bfs_maze)
        return 0