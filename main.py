from generator.maze_generator import maze_generator
from util.maze_plotter import maze_plotter
from search_algorithms.bread_first_search import breadth_first_search
import sys

# from search_algorithms.depth_first_search import depth_first_search
# from search_algorithms.a_star import a_star_search

def main(search_algorithm):
    if search_algorithm not in ["bfs", "dfs", "a-star"]:
        raise ValueError("Invalid search algorithm. Choose between 'bfs', 'dfs', or 'a-star'.")

    maze = maze_generator(100, 0.3)

    if search_algorithm == "bfs":
        path = breadth_first_search(maze)
    # elif search_algorithm == "dfs":
    #     path = depth_first_search(maze)
    # elif search_algorithm == "a-star":
    #     path = a_star_search(maze)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <search_algorithm>")
        sys.exit(1)
    search_algorithm = sys.argv[1]
    main(search_algorithm)