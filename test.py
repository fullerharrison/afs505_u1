from sys import argv
def main(*argv):
    empty_grid = [[0] * 80 for i in range(30)] # makes grid
    initiate(empty_grid, *argv)

main(*argv)
