from sys import argv

def display(row, column):
    #prints 80 x 30 'X'
    output = ''
    off = '-'
    on = str('X')
    b = 80
    a = 30
    print(row)
    board = [[off] * b for i in range(a)]

    for x, rows in enumerate(board):
        for y, columns in enumerate(rows):
            if board[x][y]:
                output += on
                pass
            else:
                print("hi")
                output += off
        output += '\n'

    print(output)
"""
def initiate(*argv):
    iterations = argv[1]
    arguement_num = len(argv[2:])
    directions = argv[2:]
    row = []
    column = []
    for i in range(arguement_num):
        position = directions[i]
        position = position.split(":")
        row.append(position[0])
        column.append(position[1])
    #display(row, column)
    display(row,column)
    #print(rows)
    #print(type(position))

    return iterations


initiate(*argv)
#50 14:40 15:42 16:39 16:40 16:43 16:44 16:45
