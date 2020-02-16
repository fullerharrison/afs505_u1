"""
Authors: Harrison Fuller
Reviewer: Joshua Freimark

###Program runs explicitly on macOS

A Python script that performs Conway's game of life in a 80x30 array
.. Module:: Project01
    :platform macOS
        :synopsis: The script will recieve user derections to turn
        'on' or 'off' cells in a grid using Moores neighborhood rules
        then print the evolution by 'ticks' also recieved by the user_
.. moduleauthor:: Harrison Fuller <harrison.fuller@wsu.edu>
.. moduleauthor:: Joshua Freimark
"""
# allow for input from terminal
from sys import argv

def neighbors(grid, row, cell):
    """
    Calculate the sum of the neighbors of element being evaluated
    :param row, cell: arguements for cells active
    :type integers: a integer object from grid

    :return: the sum of neighbors to make decision
    :rtype: integer
    """
    on_count = (grid[row-1][cell-1] + grid[row-1][cell] + grid[row-1][cell+1] +
        grid[row][cell-1] + (grid[row][cell]*0)+ grid[row][cell+1] +
        grid[row+1][cell-1] + grid[row +1][cell] + grid[row +1][cell+1])
    return on_count

def make_move( grid, nrows, ncols):
    """
    Function iterates over grid and evaluates the neigbors of '0'/'1' values
    :param grid,nrows, ncells: arguements for iterating over grid
    :type lists, integers: Array of lists, and integer object from grid

    :return: the new grid
    :rtype: Array/2-d list
    """
    new_grid = [[0] * ncols for i in range(nrows)]  # For new grid to post decisions
    for row in range(nrows-1):
        for cell in range(ncols-1):
            on_count = neighbors(grid, row, cell)
            if grid[row][cell] == 1: # If cells alive
                if (on_count == 2) or (on_count == 3):
                    new_grid[row][cell] = 1 # b. Any “on” cell with two or three “on” neighbors remains “on”.
                else: # c. Any “on” cell with more than three “on” neighbors is turned “off”.
                      # a. Any “on” cell with fewer than two live neighbors is turned “off”.
                      new_grid[row][cell] = 0

            elif grid[row][cell] == 0:  # If cells dead
                if on_count == 3:
                    new_grid[row][cell] = 1 # d. Any “off” cell with exactly three live neighbors is turned “on”.
                else:
                    new_grid[row][cell] = 0

    return new_grid
def initiate(coordinates, grid, nrows, ncols):
    """
    Function iterates over grid and implements starting coordinates
    :param coordinates,grid, nrows, ncells: arguements for: 'Alive' cells, and iterating over grid
    :type lists, lists, integers:List of integers, 2-d lists, and integer object from grid

    :return: the new grid
    :rtype: Array/2-d list
    """

    for item in coordinates:
        row, col = item.split(":")
        grid[int(row)][int(col)] = 1
    #make_move(grid, nrows, ncols)

def print_grid(grid, nrows, ncols):
    """
    Function makes grid of '-'/'X' for alive/dead cells
    :param grid, nrows, ncells: arguements for: making dimensions of 2-d structure and
    :type lists, integers: 2-d lists, and integer object from grid

    :return: the new grid
    :rtype: Array/2-d list
    """
    string_grid = ""    # empty string for terminal output
    for row in range(nrows-1) :
        for cell in range(ncols-1):
            if grid[row][cell] == 0:
                string_grid += '-' # every 0 int is replaced with '-' character
            elif grid[row][cell] == 1:
                string_grid += 'X' # every 1 int is replaced with 'X' character
        string_grid += '\n' # Indicates the end of the list
    print(string_grid)
    #initiate(coordinates, grid, nrows, ncols)

def main(*argv):
    """
    Function extracts command from terminal and prompts parsing
    :param *argv: arguements for: all arguements from terminal
    :type lists: list of all arguements

    :return: the final string grid
    :rtype: string of '-'/'X'
    """
    nrows = 31  # dimensions greater than needed to ignore values that exceed my normal list dimensions
    ncols = 81
    ticks = (int(f"{argv[1]}")) #returns a string of ticks from terminal, -1 to make only '50' iterations

    coordinates = argv[2:] # returns a string of 'coordinates from terminal'
    grid = [[0] * ncols for i in range(nrows)] # makes grid, good
    print_grid(grid, nrows, ncols) # checks string grid, good
    initiate(coordinates, grid, nrows, ncols) #forms starting coordinates, good
    print_grid(grid, nrows, ncols) #checks starting coordinates, good
    new_grid = make_move(grid, nrows, ncols) # Makes decisions, good for first iteration
    print_grid(new_grid, nrows, ncols) # check decisions, good
    while ticks > 1:    #while loop for iterations
        new_grid = make_move(new_grid, nrows, ncols)
        print_grid(new_grid, nrows, ncols)
        ticks -= 1
        print(ticks)

main(*argv)
