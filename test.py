# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(M[1][2])
#
# s = ['red', 'green', 'blue', 'white', 'black', 'yellow', 'orange', 'pink', 'purple']
# diagonal = [[s[0] + s[4] + s[8]], [s[2] + s[4] + s[6]]]
# print(colors[::-1])
# print(colors[0:3])
# print(colors[0:7:3])
# print(diagonal)
cells = '_OOOO_X_X'
row = [cells[0:3], cells[3:6], cells[6:9]]
col = [cells[0:7:3], cells[1:8:3], cells[2:9:3]]
diag1 = cells[0] + cells[4] + cells[8]
diag2 = cells[2] + cells[4] + cells[6]
diag = [diag1, diag2]
matrix = [row, col, diag]
xwin = owin = blanks = x_ = o_ = 0

print(row)
print(col)
print(diag)
print(matrix)
# Game State print
print("---------")
print("|" + " " + cells[0] +" " + cells[1] + " " + cells[2] + " " +"|")
print("|" + " " + cells[3] +" " + cells[4] + " " + cells[5] + " " +"|")
print("|" + " " + cells[6] +" " + cells[7] + " " + cells[8] + " " +"|")
print("---------")
#Loop print
for c in cells:
    if c == "X":
        x_ += 1
for c in cells:
    if c == "O":
        o_ += 1
for c in cells:
    if c == "_":
        blanks += 1
for n in matrix:
    for x in n:
        if x == "XXX":
            xwin += 1
for n in matrix:
    for x in n:
        if x == "OOO":
            owin += 1
if x_ - o_ == 1 or x_ - o_ == 0 or x_ - o_ == -1:
    if xwin + owin > 1:
        print("Impossible")
    elif xwin == 1 and owin == 0:
        print("X wins")
    elif owin == 1 and xwin == 0:
        print("O wins")
    elif xwin + owin == 0:
        if blanks == 0:
            print("Draw")
        elif blanks > 0:
            print("Game not finished")
elif x_ - o_ >= 2 or x_ - o_ <= -2:
    print("Impossible")