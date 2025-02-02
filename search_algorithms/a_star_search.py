from util.maze_plotter import maze_plotter
from util.traversable_neighbors import traversable_neighbors
import math
import numpy as np
import heapq


def a_star_path(a_star_maze, cur_node, a_star_parent):
    """
    Trace the path from the goal node to the start node using the A* search algorithm and mark the path in the maze.

    Args:
        a_star_maze (numpy.ndarray): The maze represented as a 2D numpy array where each cell can be a wall, open space, or part of the path.
        cur_node (tuple): The current node (goal node) represented as a tuple of (row, column).
        a_star_parent (list of list of tuples): A 2D list where each element is a tuple representing the parent node of the corresponding cell in the maze.

    Returns:
        None: This function modifies the maze in place and does not return any value.

    Side Effects:
        - Modifies the input maze to mark the path from the start node to the goal node with -2.
        - Prints the length of the path.
        - Calls the maze_plotter function to visualize the maze with the path.

    Example:
        a_star_path(maze, (4, 4), parent_nodes)
    """

    # Mark the goal node in the maze with -2
    a_star_maze[len(a_star_maze)-1, len(a_star_maze)-1] = -2

    # Initialize the path length count (including the start and goal nodes)
    path_length = 2

    # Set the temporary node to the current node (goal node)
    temp_node = cur_node

     # Trace back from the goal node to the start node
    while temp_node != (0,0):

        # Mark the current node in the maze with -2
        a_star_maze[temp_node] = -2

        # Get the row and column of the current node
        (i,j) = temp_node

        # Move to the parent node
        temp_node = a_star_parent[i][j]

        # Increment the path length
        path_length += 1

    # Mark the start node in the maze with -2    
    a_star_maze[0,0] = -2

    # Visualize the maze with the path
    maze_plotter(a_star_maze, "a-star", path_length)
    return


def euclidean_distance(a_star_maze):
    """
    Calculate the Euclidean distance heuristic for an A* maze.

    This function computes the Euclidean distance from each cell in the maze to the bottom-right corner of the maze.
    The Euclidean distance is used as a heuristic in the A* search algorithm to estimate the cost of the cheapest path
    from a given cell to the goal.

    Args:
        a_star_maze (list of list of int): A 2D list representing the maze where each element is a cell.

    Returns:
        np.ndarray: A 2D numpy array where each element represents the Euclidean distance from the corresponding cell
                    in the maze to the bottom-right corner of the maze.
    """

    # Initialize a 2D numpy array with zeros to store the Euclidean distances
    euclid_heuristic = np.zeros((len(a_star_maze), len(a_star_maze)))

    # Coordinates of the bottom-right corner of the maze
    (x, y) = (len(a_star_maze)-1, len(a_star_maze)-1)

    # Calculate the Euclidean distance for each cell in the maze
    for i in range(len(a_star_maze)):
        for j in range(len(a_star_maze)):
            euclid_heuristic[i,j] = math.sqrt(math.pow((x - i), 2)+ math.pow((y-j),2))
    return euclid_heuristic


def manhattan_distance(a_star_maze):
    """
    Calculate the Manhattan distance heuristic for an A* search algorithm.

    The Manhattan distance is the sum of the absolute differences of the 
    coordinates. This function generates a heuristic matrix where each 
    element represents the Manhattan distance from that point to the 
    bottom-right corner of the maze.

    Parameters:
    a_star_maze (list of list of int): The maze represented as a 2D list.

    Returns:
    numpy.ndarray: A 2D array where each element is the Manhattan distance 
    from that point to the bottom-right corner of the maze.
    """

    # Initialize a 2D numpy array with zeros to store the Manhattan distances
    manhattan_heuristic = np.zeros((len(a_star_maze), len(a_star_maze)), dtype = int)

    # Coordinates of the bottom-right corner of the maze
    (x, y) = (len(a_star_maze)-1, len(a_star_maze)-1)

    # Calculate the Manhattan distance for each cell in the maze
    for i in range(len(a_star_maze)):
        for j in range(len(a_star_maze)):
            manhattan_heuristic[i,j] = abs(x-i)+abs(y-j)
    return manhattan_heuristic


def a_star_search(a_star_maze, h="euclid", display=True):
    """
    Perform A* search algorithm on a given maze.
    Args:
        a_star_maze (list of list of int): The maze to be solved, represented as a 2D list.
        h (str, optional): The heuristic to be used for the search. 
                           "euclid" for Euclidean distance, "manhattan" for Manhattan distance. 
                           Defaults to "euclid".
        display (bool, optional): If True, display the result of the search. Defaults to True.
    Returns:
        int: 1 if a path is found, 0 otherwise.
    """

    # Create a copy of the maze to avoid modifying the original input
    a_star_maze=a_star_maze.copy()
    source, destination = (0,0), (len(a_star_maze)-1, len(a_star_maze)-1)
    
    # Check if the heuristic is Euclidean or Manhattan
    if h=="euclid":
        heuristic = euclidean_distance(a_star_maze)
    else:
        heuristic = manhattan_distance(a_star_maze)

    # Initialize the source node with a value of -1
    a_star_maze[source] = -1

    # Initialize the parent list to store the parent-child relationships
    a_star_parent = [[None for _ in range(len(a_star_maze))] for _ in range(len(a_star_maze))]

    # Initialize the A* priority queue with the source node
    a_star_p_queue = []
    heapq.heappush(a_star_p_queue, (heuristic[source],0,source))
    path_found = 0

    # Continue A* search until the priority queue is empty or the path is found
    while len(a_star_p_queue) != 0 and path_found == 0:

        # Pop the node with the lowest cost from the priority queue
        cur_heuristic, cur_cost, cur_node = heapq.heappop(a_star_p_queue)

        # Mark the current node as visited (-2)
        a_star_maze[cur_node] = -2

        # Check if the current node is the destination
        if(cur_node == destination):

            # Set the path_found flag to True
            path_found = 1
            a_star_maze[cur_node] = -1
            a_star_maze[destination] = -2

            # If the display flag is True, print the path and visualize the maze
            if display:
                print("Path Found!!!!")
                a_star_path(a_star_maze, cur_node, a_star_parent)
            return 1
        
        # Get all valid neighbors that can be traversed
        neighbors = traversable_neighbors(a_star_maze, cur_node)

        # Iterate through the neighbors to continue the A* search
        if len(neighbors) != 0:
            # Iterate through the neighbors
            for node in neighbors:
                (i,j) = node
                # Check if the neighbor hasn't been visited
                if a_star_parent[i][j] == None:
                    # Mark the parent of the neighbor and add it to the priority queue
                    a_star_parent[i][j] = cur_node
                    heapq.heappush(a_star_p_queue, ((heuristic[i,j])+cur_cost,cur_cost+1,node))

        # Mark the current node as visited (-1)
        a_star_maze[cur_node] = -1

    # If the loop completes without finding a path, return 0
    if(path_found == 0):
        a_star_maze[source] = -2
        if display:
            print("No Path found :(")
            maze_plotter(a_star_maze, "a-star")
        return 0