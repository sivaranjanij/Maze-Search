from generator.maze_generator import maze_generator
from util.maze_plotter import maze_plot_final
import sys

def main(search_algorithm):
    if search_algorithm not in ["bfs", "dfs", "a-star"]:
        raise ValueError("Invalid search algorithm. Choose between 'bfs', 'dfs', or 'a-star'.")

    maze = maze_generator(100, 0.3)
    maze_plot_final(maze, search_algorithm)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <search_algorithm>")
        sys.exit(1)
    search_algorithm = sys.argv[1]
    main(search_algorithm)