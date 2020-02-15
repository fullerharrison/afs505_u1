from sys import argv
def print_grid(empty_grid):
    output = ""
    for row in range(30) :
        for cell in range(80):
            output += empty_grid[row][cell]
    output += '\n'

def main(*argv):
    empty_grid = [[0] * 80 for i in range(30)] # makes grid
    print_grid(empty_grid)


main(*argv)
