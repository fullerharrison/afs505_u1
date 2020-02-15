"""
Authors: Harrison Fuller
Reviewer: Joshua Freimark
Program synopsis: This program implements Conway's Game of Life. This program will displays the evolution of cells
on a 30 row by 80 column grid. The user will input how many ticks/generation it wishes the game to run for as
 well as which cells it wishes to be "alive" at the start of the game. Once the the user inputs the values correctly,
 The game will run on its own. The rules and explanation of the functions will be included as you progress through
 this script.

A Python script that performs Conway's game of life in a 80x30 array
.. Module:: Project01
    :platform macOS
        :synopsis: The script will recieve user derections to turn
        'on' or 'off' cells in a gris using Moores neighborhood rules
        then print the evolution by 'ticks' also recieved by the user_
.. moduleauthor:: Harrison Fuller <harrison.fuller@wsu.edu>
.. moduleauthor:: Joshua Freimark
"""
# allow for input from terminal
from sys import argv

def neighbor(new_grid,rows, cols):
    #print(row, col)
    for i in range(rows):
        for j in range(cols):
            on_count = (new_grid[i-1][j-1] + new_grid[i-1][j] + new_grid[i-1][j+1] + new_grid[i][j -1] + new_grid[i][j+1] + new_grid[i+1][j-1] + new_grid[i +1][j] + new_grid[i +1][j+1])
    return on_count

def next_move(new_grid):
    ##
    for row_index,row in enumerate(new_grid): #
        for column_index, cell in enumerate(row): #
            count = neighbor(new_grid,row_index, column_index)
            on_count = 0
            # If alive already
            if new_grid[row_index][column_index] == 1:
                on_count += 1
                if on_count > 3:
                    new_grid[row_index][column_index] = 0
                elif on_count < 2:
                    new_grid[row_index][column_index] = 0
                else:
                    new_grid[row_index][column_index] = 1
            elif new_grid[row_index][column_index] == 0:
                on_count += 1
                if on_count == 3:
                    new_grid[row_index][column_index] = 1
                else:
                    new_grid[row_index][column_index] = 0
            return new_grid
    print(new_grid)
#    return neighbor
def display(new_grid):
    """Build a display to be printed for game.
    Uses variables to be the 'characters' -/X and passes on
    to next function for processsing.

    :param row, column: arguements for cells active
    :type row: a integer object created by the user

    :return: a array to be printed or processed
    :rtype: a list seperated /n
    """
    output = ""
    for row in new_grid:
        for column in row:
            output += column
        output += "\n"

def initiate(empty_grid, *argv):
    """
    Prompt logistics for game.
    Uses variables to identify iterations and partitions arguemts into row
    and column coordinates.
    Passes string lists of row, column into display for game.
    to next function for processsing.

    :param *argv: arguements for cells to start as active
    :type *argv: tuple that is prompted by user at terminal

    :return iterations: variable to identify loops later
    :rtype: a integer
    """
    iterations = argv[1]    # number of "steps" or iterations
    coords = argv[2:] # list of plot directions
    new_grid = empty_grid
    for item in coords:
        row, col = item.split(":")
        new_grid[int(row)-1][int(col)-1] = 1
    next_move(new_grid)

def main(*argv):
    empty_grid = [[0] * 80 for i in range(30)] # makes grid
    initiate(empty_grid, *argv)

main(*argv)
#50 14:40 15:42 16:39 16:40 16:43 16:44 16:45
"""
n = [[rows - 1] [cols -1], [rows - 1] [cols],  [rows -1] [cols+1],
    [rows] [cols -1],      [rows * 0] [cols * 0], [rows] [cols+1],
    [rows + 1] [cols -1], [rows + 1 ] [cols], [rows + 1] [cols+1]]
for i, o in enumerate(n):
    for j, k in enumerate(o):
        s += new_grid[i][j]
    print(s)
"""
