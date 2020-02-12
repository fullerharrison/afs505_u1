"""A Python script that performs Conway's game of life in a 80x30 array

.. Module:: Project01
    :platform macOS
        :synopsis: The script will recieve user derections to turn
        'on' or 'off' cells in a gris using Moores neighborhood rules
        then print the evolution by 'ticks' also recieved by the user_

.. moduleauthor:: Harrison Fuller <harrison.fuller@wsu.edu>

"""
# allow for input from terminal
from sys import argv

def display(row, column):
    """Build a display to be printed for game.
    Uses variables to be the 'characters' -/X and passes on
    to next function for processsing.

    :param row, column: arguements for cells active
    :type row: a integer object created by the user

    :return: a array to be printed or processed
    :rtype: a list seperated /n
    """
    #prints 80 x 30 'X'

    output = '' # empty string for print later
    off = '-'   # off character
    on = str('X') # on character
    b = 80 # number of columns
    a = 30  # number of rows
    print(row)  # check

    board = [[off] * b for i in range(a)]   # make board dimensions
    c = enumerate(board)

    for x, y in c:
        for m,n in enumerate(y):
            if board[x][m]:
                for i in row:
                    if i == board[x][m]:

                        output += on
                        pass
            else:
                output += off
        output += '\n'
    print(output)

def initiate(*argv):
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
    arguement_num = len(argv[2:]) # number of plot directions
    directions = argv[2:] # list of plot directions
    row = [] # empty list for rows
    column = [] # empty list for column

    # Builds row and column lists
    # Assuming orientation from the terminal is correct
    for i in range(arguement_num):
        position = directions[i]
        position = position.split(":")
        row.append(position[0])
        column.append(position[1])
    # pass arguements to make beggining display
    display(row,column)

    # for use later?
    return iterations


initiate(*argv)
#50 14:40 15:42 16:39 16:40 16:43 16:44 16:45
