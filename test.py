from sys import argv
def print_grid(grid, nrows, ncols):
    string_grid = ""
    for row in range(nrows) :
        for cell in range(ncols):
            if grid[row][cell] == 0:
                string_grid += '-'
            elif empty_grid[row][cell] == 1:
                string_grid += 'X'
        string_grid += '\n'
    print(string_grid)
def main(*argv):
    nrows = 30
    ncols = 80
    grid = [[0] * ncols for i in range(nrows)] # makes grid
    print_grid(grid, nrows, ncols)


main(*argv)
