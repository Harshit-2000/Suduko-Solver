
suduko = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

# creating grid
def grid(list):
    for i in range(len(list)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(list)):
            print(list[i][j], end=" ")

            if (j + 1) % 3 == 0 and j != 0 and j != 8:
                print("|", end=" ")
            if j == 8:
                print(" ")


# checking empty spaces or zeros
def check_emtpy(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == 0:

                return (i, j)

    return None


# passing 0 to 9 values and checking values
def valid(row, column, n, list):
    # for row
    for i in range(len(list)):
        if n == list[i][column] and n != list[row][column]:
            return False

    # for column
    for j in range(len(list)):
        if n == list[row][j] and n != list[row][column]:
            return False

    # for box

    box_x = row // 3
    box_y = column // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if list[i][j] == n and i != row and j != column:
                return False

    return True


def main(list, row=0, column=0):
    if not check_emtpy(suduko):
        return True
    else:
        row, column = check_emtpy(suduko)

    for n in range(1, 10):
        if valid(row, column, n, suduko):
            suduko[row][column] = n
            if main(suduko, row, column):
                return True
            suduko[row][column] = 0
    return False


grid(suduko)
main(suduko)
print("\n\n")
grid(suduko)
