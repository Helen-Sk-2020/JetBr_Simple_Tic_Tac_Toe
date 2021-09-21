# stage 5/5
s = '         '
matrix = [[s[0], s[1], s[2]], [s[3], s[4], s[5]], [s[6], s[7], s[8]]]
counter = 0
numbers = [str(x) for x in range(1, 10)]
print(f"---------"
      f"\n| {' '.join(matrix[0])} |"
      f"\n| {' '.join(matrix[1])} |"
      f"\n| {' '.join(matrix[2])} |"
      f"\n---------")
while True:
    if counter == 9:
        break
    else:
        x, y = input('Enter the coordinates:').split()
        # x, y = '2 2'.split()
        if x in numbers and y in numbers:
            x = int(x) - 1
            y = int(y) - 1
            if x not in range(3) or y not in range(3):
                print('Coordinates should be from 1 to 3!')
            else:
                counter += 1
                if matrix[x][y] == ' ':
                    if counter % 2 != 0:
                        matrix[x][y] = 'X'
                    else:
                        matrix[x][y] = 'O'
                    print(f"---------"
                          f"\n| {' '.join(matrix[0])} |"
                          f"\n| {' '.join(matrix[1])} |"
                          f"\n| {' '.join(matrix[2])} |"
                          f"\n---------")
                else:
                    print('This cell is occupied! Choose another one!')
        
        else:
            print('You should enter numbers!')
# print(matrix)
matrix = matrix[0] + matrix[1] + matrix[2]
s = ''.join(matrix)
row = [s[0:3], s[3:6], s[6:9]]
column = [s[0:7:3], s[1:8:3], s[2:9:3]]
diagonal = [s[0] + s[4] + s[8], s[2] + s[4] + s[6]]
matrix = [row, column, diagonal]
result = ''
x_win = o_win = 0
x_count = [x for x in s if x == 'X']
o_count = [x for x in s if x == 'O']
__count = [x for x in s if x == '_']
difference_moves = len(x_count) - len(o_count)
for y in matrix:
    for x in y:
        if x == 'XXX':
            x_win += 1
        elif x == 'OOO':
            o_win += 1
if difference_moves not in range(-1, 2):
    result = 'Impossible'
elif x_win >= 1:
    if o_win == 0:
        result = 'X wins'
    else:
        result = 'Impossible'
elif o_win >= 1:
    if x_win == 0:
        result = 'O wins'
    else:
        result = 'Impossible'
elif len(__count) == 0:
    result = 'Draw'
elif len(__count) > 0:
    result = 'Game not finished'
else:
    result = 'Impossible'
print(result)
