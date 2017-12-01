#!/usr/bin/env python3

# Requires pillow, the Python3 version of PIL
# Be sure to pip3 pillow
from PIL import Image
import random
from common_input import input_int

# Bit field values for directions
LEFT = 1
DOWN = 2
RIGHT = 4
UP = 8

# Maze dimensions
CELL_WIDTH = 16

# Image colors
WALL_COLOR = (0, 0, 0)
FLOOR_COLOR = (255, 255, 255)


# TODO: put this into a class to clean up some logic (shared state, recalculated values)


def generate_maze(width, height):
    # Initialize grid.  Start state is with each cell having no openings.
    grid = [[0 for _ in range(width+2)] for _ in range(height+2)]

    # Create the outer wall of the maze.  Each outer cell has openings to the other cells, except
    # into the main body of the maze.
    for x in range(0, width+2):
        grid[0][x] = LEFT+RIGHT+UP
        grid[height+1][x] = LEFT+RIGHT+DOWN
    for y in range(0, height+2):
        grid[y][0] |= LEFT+UP+DOWN
        grid[y][width+1] |= RIGHT+UP+DOWN

    # Generate maze from random starting point on the top.  Use "hunt and kill" maze gen algorithm.
    maze_start = random.randint(1, width-1)
    x = maze_start
    y = 1
    done = False
    while not done:
        grid = fill_maze_from(x, y, grid)   # Fill maze until a dead-end is hit
        x, y = hunt(grid)             # Look for empty spots to continue to gen maze
        done = x is None

    # Create openings on top and bottom.
    # TODO: be smart about where to put bottom exit to maximize maze length
    grid[1][maze_start] += UP
    grid[0][maze_start] += DOWN
    maze_end = random.randint(2, width-1)
    grid[height][maze_end] += DOWN
    grid[height+1][maze_end] += UP

    return grid


def get_neighbors_random(x, y, grid):
    """
    :return: A randomly ordered list of the neighbor cells of (x, y).  Each element is a tuple with 4 values:
    neighbor x - the x-value of the neighbor cell
    neighbor y - the y-value of the neighbor cell
    direction - the direction from (x, y) to the neighbor cell
    opposite - the direction from the neighbor cell to (x, y)
    """
    neighbors = [(x - 1, y, LEFT, RIGHT), (x, y + 1, DOWN, UP), (x + 1, y, RIGHT, LEFT), (x, y - 1, UP, DOWN)]
    random.shuffle(neighbors)
    return neighbors


def fill_maze_from(x, y, grid):
    """
    From the start point, create a path using cells that have not been previously visitied.  Returns when a
    dead-end is reached.
    :return: Grid with values for open passage ways
    """
    foundNeighbor = True  # this is logically a "do...while", but since this is Python, we'll fake it.
    while foundNeighbor:
        foundNeighbor = False
        neighbors = get_neighbors_random(x, y, grid)
        # Look for a neighbor (in bounds) that has not already been visited
        for new_x, new_y, direction, opposite in neighbors:
            if 1 <= new_x <= len(grid[0]) - 2 and 1 <= new_y <= len(grid) - 2 and grid[new_y][new_x] == 0:
                # Next cell found.  Connect to new cell, and continue filling from that new cell.
                foundNeighbor = True
                grid[y][x] += direction
                grid[new_y][new_x] = opposite
                x = new_x
                y = new_y
                break
    return grid


def hunt(grid):
    """
    Look for a place to start a new path.  It needs to be an unvisited cell that has at least
    one visited neighbor.  Returns a tuple with a new cell to draw a path from.
    """
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                neighbors = get_neighbors_random(x, y, grid)
                for new_x, new_y, direction, opposite in neighbors:
                    if 1 <= new_x <= len(grid[0]) - 2 and 1 <= new_y <= len(grid) - 2 and grid[new_y][new_x] != 0:
                        grid[y][x] += direction
                        grid[new_y][new_x] += opposite
                        return x, y
    return None, None


def convert_to_bitmap(maze):
    """
    Creates a bitmap from a generated mazer
    """

    # Initialize the bitmap.  Each maze cell is CELL_WIDTH squared.
    pixel_grid = [[FLOOR_COLOR for _ in range(CELL_WIDTH * len(maze[0]))] for _ in range(CELL_WIDTH * len(maze))]

    for maze_y in range(len(maze)):
        for maze_x in range(len(maze[0])):
            # For each cell, draw walls.  Remember the data in each cell denotes PATHWAYS not walls
            if not maze[maze_y][maze_x] & LEFT:
                for y in range(CELL_WIDTH):
                    pixel_grid[CELL_WIDTH*maze_y+y][CELL_WIDTH*maze_x] = WALL_COLOR
            if not maze[maze_y][maze_x] & DOWN:
                for x in range(CELL_WIDTH):
                    pixel_grid[CELL_WIDTH*maze_y+CELL_WIDTH-1][CELL_WIDTH*maze_x+x] = WALL_COLOR
            if not maze[maze_y][maze_x] & RIGHT:
                for y in range(CELL_WIDTH):
                    pixel_grid[CELL_WIDTH*maze_y+y][CELL_WIDTH*maze_x+CELL_WIDTH-1] = WALL_COLOR
            if not maze[maze_y][maze_x] & UP:
                for x in range(CELL_WIDTH):
                    pixel_grid[CELL_WIDTH*maze_y][CELL_WIDTH*maze_x+x] = WALL_COLOR
    return pixel_grid


def save_bitmap(bitmap, filename):
    # Convert 2D bitmap to 1D array of pixels
    # TODO: does PIL take a 2D array?
    pixel_list = []
    for pixel_y in range(len(bitmap)):
        for pixel_x in range(len(bitmap[0])):
            pixel_list.append(bitmap[pixel_y][pixel_x])

    # Create and save image
    img = Image.new("RGB", (len(bitmap[0]), len(bitmap)))
    img.putdata(pixel_list)
    img.save(filename)


def main():
    random.seed()
    print("Maze generator")
    width = input_int("Width? ", 3, 500)
    height = input_int("Height? ", 3, 500)
    maze = generate_maze(width, height)
    print("Maze generated.")
    filename = input("File name? ")
    bitmap = convert_to_bitmap(maze)
    save_bitmap(bitmap, filename)
    print(f"Maze saved to {filename}")


# Run the program
if __name__ == "__main__":
    main()
