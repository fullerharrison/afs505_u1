
def display(w, h):
    width = 80
    height = 30

    output = ''

    for y, row in enumerate(self.board, start = 1):
        for x, cell in enumerate(row, start = 1):
            if self.board[y][x]:
                output += 'X'
            else:
                output += '-'
        output += '\n'
    print(output)
    pass

display(input(), input())
