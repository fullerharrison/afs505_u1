from sys import argv
def main(*argv):
    empty_grid = [[0] * 80 for i in range(30)] # makes grid
    print_grid(empty_grid)

def print_grid(empty_grid):
    output = ""
    for row_index, row in enumerate(empty_grid) :
        for column_index, cell in enumerate(row):
            output += empty_grid[row_index][column_index]
    output += '\n'
main(*argv)
