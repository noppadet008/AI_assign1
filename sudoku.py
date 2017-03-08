from tkinter import Tk
from tkinter.filedialog import askopenfilename


def print_table(table):
    for i in range(0, 9):
        for j in range(0, 9):
            print(table[i][j], end=" ")
            if (j+1) % 3 == 0:
                print("| ", end="")
        print()
        if (i+1) % 3 == 0:
            print("- "*12)


def check_table(table, x, y):
    # check in block.
    collection_test = [True] * 9
    init_x = x // 3 * 3  # to get point to start iterate row.
    init_y = y // 3 * 3 # to get point to start iterate column.
    for i in range(0, 3):
        for j in range(0, 3):
            num = int(table[init_x + i][init_y + j]) - 1
            if num == -1:
                continue
            elif collection_test[num]:
                collection_test[num] = False
            else:
                return False

    # check in row.
    collection_test = [True] * 9
    for i in range(0, 9):
        num = int(table[i][y]) - 1
        if num == -1:
            continue
        elif collection_test[num]:
            collection_test[num] = False
        else:
            return False

    # check in column.
    collection_test = [True] * 9
    for i in range(0, 9):
        num = int(table[x][i]) - 1
        if num == -1:
            continue
        elif collection_test[num]:
            collection_test[num] = False
        else:
            return False

    return True

def import_file():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    print("open => " + filename)

    file = open(filename, "r")
    data = [[0 for x in range(9)] for y in range(9)]
    temp = file.read().splitlines()
    for i in range(0, 9):
        data[i] = temp[i].split(",")
    return data

# print_table(data)
# for i in range(0, 9):
#     for j in range(0, 9):
#         print(str(i)+"+"+str(j),end=" => ")
#         print(check_table(data,i,i))


