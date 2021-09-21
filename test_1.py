s = '         '
matrix = [[s[0], s[1], s[2]], [s[3], s[4], s[5]], [s[6], s[7], s[8]]]
counter = 0
numbers = [str(x) for x in range(1, 10)]
while True:
    for x in matrix:
        if x == ' ':
            break

    x, y = input('Enter the coordinates:').split()
    # x, y = '3 1'.split()
    if x in numbers and y in numbers:
        x = int(x) - 1
        y = int(y) - 1
        if x not in range(3) or y not in range(3):
            print('Coordinates should be from 1 to 3!')
        else:
            counter += 1
            if matrix[x][y] != ' ':
                if counter % 2 != 0:
                    matrix[x][y] = 'X'
                else:
                    matrix[x][y] = 'O'
                print(f"---------"
                      f"\n| {' '.join(matrix[0])} |"
                      f"\n| {' '.join(matrix[1])} |"
                      f"\n| {' '.join(matrix[2])} |"
                      f"\n---------")