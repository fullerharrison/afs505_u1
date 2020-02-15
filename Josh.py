"""A Python script that attempts to replicate Conway's Game of Life.

..  module:: Game_of_life.py
    :platform: Windows, Mac, Unix
    :synopsis: This script will displays the evolution of cells on a 30 row by 80 column grid.
        The user will input how many ticks/generation it wishes the game to run for. In the same input line
         the user will specify the cells it wishes to be "alive" at the start of the game. Once the the user inputs
         the values correctly, the game will begin and run on its own. The rules and explanation of the functions
         will be included as you progress to the functions within this script.

..  moduleauthors: Joshua Freimark and Evan Stowe, Joshua.freimark@wsu.edu
..  modulereviewer: Harrison
..  reviewergrade:
"""
from sys import argv

def game_rules(r, c, grid):
    """ determines_cell_state defines the rules of the game
    :param r: Int - Row coordinate value
    :param c: Int - Column coordinate value
    :param grid: Dict - Dictionary that stores the values of the rows and columns
    """
    #Boolean values will determine if cells are on "1", or off  "0". Initial state is set to 0 for all cells
    cell_state = 0
    #n is the sum of live neighbors
    print(grid[r,c]) # returns first iteration i, j or 1,1
    for i in range(r):

        n = find_neighbors(r, c, grid)
        #Rule A. Any “on” cell with two or three “on” neighbors remains “on”.
        if grid[r,c] == 'X' and n < 2 :
            cell_state = 0
        #Rule B. Any “on” cell with two or three “on” neighbors remains “on”.
        elif grid[r,c] == 'X' and (n == 2 or n == 3):
            cell_state = 1
        #Rule C. Any “on” cell with more than three “on” neighbors is turned “off”.
        elif grid[r,c] == 'X' and n > 3:
            cell_state = 0
        #Rule D. Any “off” cell with exactly three live neighbors is turned “on”.
        if grid[r,c] == '-' and n == 3:
            cell_state = 1
    return cell_state

def find_neighbors(r, c, grid):
    """
    Finds the live neighbors for each cell.
    :param r: Int - Row coordinate to be observed
    :param c: Int - Column coordinate to be observed
    :param grid: Dict of Int - Values of the rows and columns to be stored in the grid dictionary
    """
    neighbors = call_neighbors(r, c)
    #Start with 0 on neighbor cells
    on_neighbors = 0
    for x in neighbors:
        if grid[x] ==1:
            on_neighbors += 1
    return on_neighbors

def call_neighbors(r,c):
    """
    :param r: Int - Row coordinate
    :param c: Int -Column coordinate
    :return: tuple of cell neighbors
    """
    neighbors = []
    if r != 1: ### if row is not equal to 1?? What about the first row?
        [(r-1,c-1),(r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1,c-1), (r+1,c), (r+1, c+1)]
        return neighbors
def new_grid(grid):
    new_grid = {}
    for r in range(1, 31):
        for c in range(1,81):
            #print(r,c) #print(values of range X times)
            new_grid[r,c] = game_rules(r, c, grid) ### Comment what is going on here
    return new_grid

def display(grid):
    """
    The display function recieves grid coordinates and prints the grid to the terminal
    :param grid: Int[][] - The list that is used as the game of life grid display
    """
    for r in range(1, 31): ### Hard-coding all the ranges, could opt for single variables
        #Set grid_row as empty string variable
        grid_row = ''
        for c in range(1,81):
            grid_row = grid_row + grid[r,c]
        print(grid_row)

def initiate_grid(seeds):
    """
    Create the initial grid and define the dimmensions of the grids.
    :param seeds: Int - The coordinates on the grid the user will input to start the game as on cells.
    :variable grid: Dict - Creates an empty dictonary.
    :return: Dict of Int -  grid is returned
    """
    grid = {}
    for r in range(1, 31):
        for c in range(1, 81):
            #Populate the grid with '-' cells which denotes that cell is turned off.
            grid[r,c] = "-"
    #Loop through seeds and insert a "X" in the r,c which denotes the cell is turned on.
    for r,c in seeds:
        grid[r,c] = 'X'
        return grid
def translate_input(input_string):
    """
    Accepts user input and converts it to an integer and stores it in list.
    translate_input will recieve input from the user and convert it to an internger.
    :param ticks: Int - The number of generations the game will run.
    :param user_input: String - The number of row:column the user wishes to turn on in the first generation.
    """
    user_inputs = input_string.split()    #This will split the user inputs with a single space.
    generations = (int(user_inputs[0]))   # The first object of the user_inputs will be the generations and it is seperated from the remaining input.
    user_inputs = user_inputs[1:]   # The remaining input values will be used to display the on cells on the grid.
    user_seeds = []   # user_seeds is an empty list for now
    for user_input in user_inputs:
        row_string, column_string = user_input.split(":")  #The row and column will be split by a colon character ":".
        user_seeds.append((int(row_string), int(column_string)))    #Convert row_string and column_string to integers and append them to the user_seed list.
    return generations, user_seeds    # returns the ticks/generations as well as the location of user_side in row_column format

def input_function():
    """Will accept user input and display the output on the grid in the terminal"""
    print("Input an integer (1-100) for the number of generations for the game to run.")
    print("In the same line, seperated by a space, input the coordinates of the grid")
    print("that you want to start as on cells. Use the format row:column.")
    print("Row range: 1-30")
    print("Column range: 1-80")
    print("\n")
    print("Example:10 14:40 15:42")
    #User will input the number of generations for the game to run
    generations_user_seeds = input(">")
    generations, coordinate = translate_input(generations_user_seeds)
    Show_grid = initiate_grid(coordinate) ### Breaks after the first try
    display(Show_grid)
    while generations > 0:
        #Decrease the number of generations by 1 while the game is operating
        generations -= 1
        input('>') ### this input does nothing
        Show_grid = new_grid(Show_grid)
input_function()
