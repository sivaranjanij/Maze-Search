from generator.maze_generator import maze_generator
from util.maze_plotter import maze_plotter
from search_algorithms.bread_first_search import breadth_first_search
from search_algorithms.depth_first_search import depth_first_search
import argparse


# from search_algorithms.a_star import a_star_search

def main(search_algorithm):
    maze = maze_generator(100, 0.3)

    if search_algorithm == "bfs":
        path = breadth_first_search(maze)
    elif search_algorithm == "dfs":
        path = depth_first_search(maze)
    # elif search_algorithm == "a-star":
    #     path = a_star_search(maze)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maze Search Algorithm")
    parser.add_argument("--algorithm", required=True, choices=["bfs", "dfs", "a-star"], help="Search algorithm to use")
    args = parser.parse_args()

    search_algorithm = args.algorithm
    main(search_algorithm)